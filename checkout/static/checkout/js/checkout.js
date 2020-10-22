let countrySelected = $('#id_country').val();
if (!countrySelected) {
    $('#id_country').css('color', '#aab7c4');
};
$('#id_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});

let appSelected = $('#id_app').val();
if (appSelected != 'select') {
    $('#id_app').css('color', '#000');
} else {
    $('#id_app').css('color', '#aab7c4');
};
$('#id_app').change(function () {
    appSelected = $(this).val();
    if (appSelected != 'select') {
        $(this).css('color', '#000');
    } else {
        $(this).css('color', '#aab7c4');
    }
});

