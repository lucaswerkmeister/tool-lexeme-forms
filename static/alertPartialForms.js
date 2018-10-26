document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    const template = JSON.parse(document.getElementsByTagName('main')[0].dataset.template),
          baseUrl = document.querySelector('link[rel=index]').href,
          inputs = Array.from(document.querySelectorAll('input[name="form_representation"]')),
          addAlert = _.once(() => {
              const url = `${baseUrl}api/v1/advanced_partial_forms_hint/${template.language_code}`,
                    init = {
                        headers: {
                            Accept: 'text/html'
                        }
                    };
              return fetch(url, init).then(response => response.text()).then(partialFormsHintHtml => {
                  const partialFormsHint = document.createElement('div');
                  document.querySelector('form').insertAdjacentElement('beforebegin', partialFormsHint);
                  partialFormsHint.outerHTML = partialFormsHintHtml;
              });
          });

    inputs.forEach(input => input.addEventListener('invalid', e => {
        if (inputs.some(input => input.value === ''))
            addAlert();
    }));
});
