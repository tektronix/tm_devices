document.addEventListener('DOMContentLoaded', function () {
    // Selects all h2 elements within divs that have both the "doc" and "doc-children" classes
    var headings = document.querySelectorAll('.doc.doc-children h2');

    headings.forEach(function(heading) {
        var hr = document.createElement('hr'); // Creates a new <hr> element
        // Inserts the <hr> element before the current h2 element
        heading.parentNode.insertBefore(hr, heading);
    });
});
