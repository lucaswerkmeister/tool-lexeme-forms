document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    const template = JSON.parse(document.getElementsByTagName('main')[0].dataset.template),
          baseUrl = document.querySelector('link[rel=index]').href,
          form = document.forms[0],
          lemmaInput = form.elements['form_representation'][0] || form.elements['form_representation'],
          lexemeIdInput = (form.elements['lexeme_id'] || [])[0];

    function removeElementById(id) {
        const element = document.getElementById(id);
        if (element) {
            element.remove();
        }
    }

    function checkDuplicates(e) {
        removeElementById('duplicates-warning');
        removeElementById('no-duplicate');

        const lemma = e.target.value.split('/', 1)[0];
        if (lemma === '') {
            return;
        }

        if (lexemeIdInput && lexemeIdInput.value) {
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
                return;
            }

            const url = `${baseUrl}api/v1/no_duplicate/${template.language_code}`;
            return fetch(url, init).then(response => response.text()).then(noDuplicateHtml => {
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
    lemmaInput.addEventListener('input', checkDebounced);
    lemmaInput.addEventListener('change', checkDebounced.flush);

    checkDuplicates({ target: lemmaInput });
});
