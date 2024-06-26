document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    const template = JSON.parse(document.getElementsByTagName('main')[0].dataset.template),
          uselang = document.documentElement.dataset.uselang,
          baseUrl = document.querySelector('link[rel=index]').href,
          form = document.forms[0],
          lexemeIdInput = (form.elements['lexeme_id'] || [])[0],
          initAcceptHtml = {
              headers: {
                  Accept: 'text/html'
              }
          };
    let formRepresentationInputs = form.elements['form_representation'];
    if (formRepresentationInputs.length === undefined) {
        formRepresentationInputs = [ formRepresentationInputs ];
    }

    let lastCheckedLemma = null;
    let cachedNoDuplicateHtml = null;

    function removeElementById(id) {
        const element = document.getElementById(id);
        if (element) {
            element.remove();
        }
    }

    function removeDuplicatesElements() {
        removeElementById('duplicates-warning');
        removeElementById('no-duplicate');
    }

    /**
     * Get the lemma for the lexeme from the given form data.
     *
     * The lemma is the first nonempty form representation variant
     * of a form that has 'lemma': true set,
     * or else the first nonempty form representation variant of any form.
     * (Supporting other froms to become the lemma is neeedd for advanced mode,
     * where any form may be omitted, which is useful for e.g. pluralia tantum.)
     *
     * This logic is duplicated in app.py::get_lemma and app.py::update_lexeme() –
     * keep the different versions in sync!
     */
    function getLemma(formRepresentationInputs) {
        for (let i = 0; i < formRepresentationInputs.length; i++) {
            const form = template.forms[i];
            if (form.lemma !== true) {
                continue;
            }
            const formRepresentationInput = formRepresentationInputs[i];
            for (const formRepresentationVariant of formRepresentationInput.value.split('/')) {
                if (formRepresentationVariant !== '') {
                    return formRepresentationVariant;
                }
            }
        }

        for (const formRepresentationInput of formRepresentationInputs) {
            for (const formRepresentationVariant of formRepresentationInput.value.split('/')) {
                if (formRepresentationVariant !== '') {
                    return formRepresentationVariant;
                }
            }
        }

        return null;
    }

    function noDuplicateHtml() {
        if (cachedNoDuplicateHtml !== null) {
            return Promise.resolve(cachedNoDuplicateHtml);
        }

        const url = `${baseUrl}api/v1/no_duplicate?uselang=${uselang}`;
        return fetch(url, initAcceptHtml).then(response => response.text()).then(noDuplicateHtml => {
            if (cachedNoDuplicateHtml === null) {
                cachedNoDuplicateHtml = noDuplicateHtml;
            }
            return cachedNoDuplicateHtml;
        });
    }

    function checkDuplicates() {
        if (lexemeIdInput && lexemeIdInput.value) {
            removeDuplicatesElements();
            return;
        }

        const lemma = getLemma(formRepresentationInputs);

        if (lemma === lastCheckedLemma) {
            return;
        }
        lastCheckedLemma = lemma;

        if (lemma === null) {
            removeDuplicatesElements();
            return;
        }

        const wiki = 'test' in template ? 'test' : 'www';
        const lang = template.language_code;
        const encodedLemma = encodeURIComponent(lemma).replace(/^\./, '%2E');
        const templateName = template['@template_name'];
        let url = `${baseUrl}api/v1/duplicates/${wiki}/${lang}/${encodedLemma}?template_name=${templateName}`;
        if (template.target_hash) {
            url += `&target_hash=${template.target_hash}`;
        }
        url += `&uselang=${uselang}`;
        fetch(url, initAcceptHtml).then(response => {
            if (response.ok) {
                return response.text();
            } else {
                // just bail out and let server-side no-JS duplicate detection take over
                throw response;
            }
        }).then(duplicatesWarningHtml => {
            if (duplicatesWarningHtml === '') {
                removeDuplicatesElements();
                return;
            }

            return noDuplicateHtml().then(noDuplicateHtml => {
                if (lemma !== lastCheckedLemma) {
                    // it changed in the meantime, maybe the network request was slow
                    return;
                }

                removeDuplicatesElements();

                const duplicatesWarning = document.createElement('div');
                form.insertAdjacentElement('afterbegin', duplicatesWarning);
                duplicatesWarning.outerHTML = duplicatesWarningHtml;

                const noDuplicate = document.createElement('label');
                document.getElementById('submit').insertAdjacentElement('beforebegin', noDuplicate);
                noDuplicate.outerHTML = noDuplicateHtml;

                for (const link of form.getElementsByTagName('a')) {
                    if (link.href.startsWith(`${baseUrl}template/${template['@template_name']}/edit/`)) {
                        function addFormDataToLink() {
                            const params = new URLSearchParams(link.search);
                            params.delete('form_representation');
                            for (const formRepresentationInput of formRepresentationInputs) {
                                params.append('form_representation', formRepresentationInput.value);
                            }
                            link.search = params;
                        }
                        link.addEventListener('click', addFormDataToLink);
                        link.addEventListener('auxclick', addFormDataToLink);
                    }
                }
            });
        }).catch(console.error);
    }

    const checkDebounced = _.debounce(checkDuplicates, 500);
    for (const formRepresentationInput of formRepresentationInputs) {
        formRepresentationInput.addEventListener('input', checkDebounced);
        formRepresentationInput.addEventListener('change', checkDebounced.flush);
    }

    checkDuplicates();
});
