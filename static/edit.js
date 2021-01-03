document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    document.documentElement.classList.add('draggable')

    let draggedElement = null;

    function dragstart(event) {
        draggedElement = event.target;
        document.documentElement.classList.add('dragging')
    }

    function drop(event) {
        const url = event.dataTransfer.getData('text/plain');
        const match = url.match(/Lexeme:(L[1-9][0-9]*)#(F[1-9][0-9]*)$/);
        if (match === null ) {
            return;
        }
        const [full_match, lexeme_id, form_id] = match;
        if (event.target.value !== '') {
            event.target.value += '/';
        }
        event.target.value += lexeme_id + '-' + form_id;
        event.preventDefault();

        const link = draggedElement;
        const listItem = link.parentElement;
        const list = listItem.parentElement;
        const alert = list.parentElement;
        listItem.remove();
        if (list.childElementCount === 0) {
            alert.remove();
        }

        dragend(event);
    }

    function dragend(event) {
        draggedElement = null;
        document.documentElement.classList.remove('dragging');
    }

    window.addEventListener('dragstart', dragstart);
    document.querySelectorAll('input[name=form_representation]').forEach(element => element.addEventListener('drop', drop));
    window.addEventListener('dragend', dragend);
});
