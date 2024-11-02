document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    const template = JSON.parse(document.getElementsByTagName('main')[0].dataset.template),
          templateName = template['@template_name'],
          baseUrl = document.querySelector('link[rel=index]').href,
          form = document.forms[0],
          wikifunctionsButtonsContainer = document.getElementById('wikifunctions-buttons'),
          wikifunctionsMessageGenerating = document.getElementById('wikifunctions-generating'),
          wikifunctionsMessageError = document.getElementById('wikifunctions-error');
    if (!wikifunctionsButtonsContainer) {
        return;
    }
    let formRepresentationInputs = form.elements['form_representation'];
    if (formRepresentationInputs.length === undefined) {
        formRepresentationInputs = [ formRepresentationInputs ];
    }
    if (!formRepresentationInputs[0]) {
        return; // no forms?
    }

    const functionNames = new Set();
    for (const form of template.forms) {
        for (const functionName in form.wikifunctions) {
            functionNames.add(functionName);
        }
    }

    function setAllButtonsDisabled(disabled) {
        for (const button of buttons) {
            button.disabled = disabled;
        }
    }
    function hideAllMessages() {
        wikifunctionsMessageGenerating.style.display = 'none';
        wikifunctionsMessageError.style.display = 'none';
    }

    const buttons = [];
    for (const functionName of functionNames) {
        const button = document.createElement('button');
        button.textContent = functionName;
        button.classList.add('btn', 'btn-outline-info');
        button.addEventListener('click', () => {
            let lemma = formRepresentationInputs[0].value.split('/').filter(s => s)[0];
            if (!lemma) {
                // no first form to generate others from yet; can we fill it from the lemma?
                if ('_edit_mode' in form.elements) {
                    const lemmaInLanguage = document.querySelector(`#lemmas [lang="${template.language_code}"]`);
                    if (lemmaInLanguage && lemmaInLanguage.textContent) {
                        lemma = lemmaInLanguage.textContent;
                        formRepresentationInputs[0].value = lemma;
                    }
                }
            }
            if (!lemma) {
                return;
            }
            setAllButtonsDisabled(true);
            hideAllMessages();
            wikifunctionsMessageGenerating.style.display = 'inline';
            fetch(`${baseUrl}/api/v1/wikifunctions/${templateName}/${lemma}/${functionName}`)
                .then(r => r.json())
                .then(response => {
                    for (let i = 0; i < response.length; i++) {
                        let value = response[i];
                        if (value === null ) {
                            continue;
                        } else if (Array.isArray(value)) {
                            value = value.join('/');
                        }
                        if (formRepresentationInputs[i] && !formRepresentationInputs[i].value) {
                            formRepresentationInputs[i].value = value;
                        }
                    }
                    hideAllMessages();
                })
                .catch(e => {
                    hideAllMessages();
                    wikifunctionsMessageError.style.display = 'inline';
                    console.error(e);
                })
                .then(() => setAllButtonsDisabled(false));
        });
        wikifunctionsButtonsContainer.append(button);
        buttons.push(button);
    }
});
