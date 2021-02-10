document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    for (const form of document.forms) {
        let lastSubmit = null;
        form.addEventListener('submit', (e) => {
            if (lastSubmit && (Date.now() - lastSubmit) < 5000) {
                e.preventDefault();
            } else {
                lastSubmit = Date.now();
            }
        });
    }
});
