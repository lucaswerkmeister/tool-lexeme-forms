document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    const template = JSON.parse(document.getElementsByTagName('main')[0].dataset.template),
          baseUrl = document.querySelector('link[rel=index]').href,
          form = document.forms[0],
          wikifunctionsContainer = document.getElementById('wikifunctions');
    if (!wikifunctionsContainer) {
        return;
    }
    let formRepresentationInputs = form.elements['form_representation'];
    if (formRepresentationInputs.length === undefined) {
        formRepresentationInputs = [ formRepresentationInputs ];
    }

    const functionNames = new Set();
    for (const form of template.forms) {
        for (const functionName in form.wikifunctions) {
            functionNames.add(functionName);
        }
    }

    for (const functionName of functionNames) {
        const button = document.createElement('button');
        button.textContent = functionName;
        button.classList.add('btn', 'btn-outline-info');
        button.addEventListener('click', () => {
            if (!formRepresentationInputs[0] || !formRepresentationInputs[0].value) {
                return; // no first form to generate others from
            }
            const templateName = template['@template_name'];
            const lemma = formRepresentationInputs[0].value;
            fetch(`${baseUrl}/api/v1/wikifunctions/${templateName}/${functionName}/${lemma}`)
                .then(r => r.json())
                .then(response => {
                    for (let i = 0; i < response.length; i++) {
                        if (formRepresentationInputs[i] && !formRepresentationInputs[i].value) {
                            formRepresentationInputs[i].value = response[i];
                        }
                    }
                });
        });
        wikifunctionsContainer.append(button);
    }
});
