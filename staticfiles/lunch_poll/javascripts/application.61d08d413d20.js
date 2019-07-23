import './shared.js';
import './jquery.formset.js' as formset();

$('.formset_row-{{ formset.prefix }}').formset({
    addText: 'add another',
    deleteText: 'remove',
    prefix: '{{ formset.prefix }}',
});
