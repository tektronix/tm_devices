document.addEventListener('DOMContentLoaded', function () {
    var properties = document.querySelectorAll('dl.py.property');
    properties.forEach(function (prop) {
        var br = document.createElement('br');
        prop.parentNode.insertBefore(br, prop.nextSibling);
    });
});
