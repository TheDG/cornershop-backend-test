import './shared.js';
import './jquery.formset.js';

$('.formset_row-{{ formset.prefix }}').formset({
    addText: 'add another',
    deleteText: 'remove',
    prefix: '{{ formset.prefix }}',
});
