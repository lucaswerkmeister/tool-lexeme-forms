document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    const template = JSON.parse(document.getElementsByTagName('main')[0].dataset.template),
          baseUrl = document.querySelector('link[rel=index]').href;

    function removeElementById(id) {
        const element = document.getElementById(id);
        if (element) {
            element.remove();
        }
    }

    document.querySelector('input[name=form_representation]').addEventListener('change', e => {
        removeElementById('duplicates-warning');
        removeElementById('no-duplicate');

        const lemma = e.target.value;
        if (lemma === '') {
            return;
        }

        const url = `${baseUrl}api/v1/duplicates/${'test' in template ? 'test' : 'www'}/${template.language_code}/${lemma}`,
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
            fetch(url, init).then(response => response.text()).then(noDuplicateHtml => {
                const duplicatesWarning = document.createElement('div');
                document.querySelector('form').insertAdjacentElement('beforebegin', duplicatesWarning);
                duplicatesWarning.outerHTML = duplicatesWarningHtml;

                const noDuplicate = document.createElement('label');
                document.querySelector('form dl').insertAdjacentElement('afterend', noDuplicate);
                noDuplicate.outerHTML = noDuplicateHtml;
            });
        });
    });
});
