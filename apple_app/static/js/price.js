//    var priceElement = document.getElementById('formatted-price');
//    var priceValue = parseFloat(priceElement.textContent.split(' ')[1].replace(',', ''));
//    priceElement.textContent = 'Price: ' + priceValue.toLocaleString() + ' VND';
//
    document.addEventListener('DOMContentLoaded', function () {
        var priceElements = document.querySelectorAll('.price');

        priceElements.forEach(function (element) {
            var priceValue = parseFloat(element.textContent.split(' ')[1].replace(',', ''));
            element.textContent = 'Price: ' + priceValue.toLocaleString() + ' VND';
        });
    });