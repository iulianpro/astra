let countrySelected = $('#id_default_country').val();
if (!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
$('#id_default_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});

let appSelected = $('#id_default_app').val();
if (appSelected != 'select') {
    $('#id_default_app').css('color', '#000');
} else {
    $('#id_default_app').css('color', '#aab7c4');
};
$('#id_default_app').change(function () {
    appSelected = $(this).val();
    if (appSelected != 'select') {
        $(this).css('color', '#000');
    } else {
        $(this).css('color', '#aab7c4');
    }
});
