document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    const menu = document.getElementById('collapsible-menu');
    menu.classList = 'collapse navbar-collapse';

    const button = document.querySelector('nav .navbar-toggler');
    button.hidden = false;
    button.addEventListener('click', () => { menu.classList.toggle('show') });
});
