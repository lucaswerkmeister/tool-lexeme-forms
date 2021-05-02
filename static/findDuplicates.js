document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    const template = JSON.parse(document.getElementsByTagName('main')[0].dataset.template),
          baseUrl = document.querySelector('link[rel=index]').href,
          form = document.forms[0],
          lexemeIdInput = (form.elements['lexeme_id'] || [])[0];
    let formRepresentationInputs = form.elements['form_representation'];
    if (formRepresentationInputs.length === undefined) {
        formRepresentationInputs = [ formRepresentationInputs ];
    }

    let lastCheckedLemma = null;

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
     * The lemma is the first nonempty form representation variant.
     * (Usually, the first representation variant of the first form,
     * but in advanced mode, any form may be omitted, including the first one,
     * which can be useful for e.g. pluralia tantum.)
     *
     * This logic is duplicated in app.py::get_lemma –
     * keep the two in sync!
     */
    function getLemma(formRepresentationInputs) {
        for (const formRepresentationInput of formRepresentationInputs) {
            for (const formRepresentationVariant of formRepresentationInput.value.split('/')) {
                if (formRepresentationVariant !== '') {
                    return formRepresentationVariant;
                }
            }
        }
        return null;
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

        const url = `${baseUrl}api/v1/duplicates/${'test' in template ? 'test' : 'www'}/${template.language_code}/${encodeURIComponent(lemma)}?template_name=${template['@template_name']}`,
              init = {
                  headers: {
                      Accept: 'text/html'
                  }
              };
        fetch(url, init).then(response => response.text()).then(duplicatesWarningHtml => {
            if (duplicatesWarningHtml === '') {
                removeDuplicatesElements();
                return;
            }

            const url = `${baseUrl}api/v1/no_duplicate/${template.language_code}`;
            return fetch(url, init).then(response => response.text()).then(noDuplicateHtml => {
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
                            for (const form_representation of form.elements['form_representation']) {
                                params.append('form_representation', form_representation.value);
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
