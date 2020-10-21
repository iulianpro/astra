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
if (appSelected) {
    $('#id_default_app').css('color', '#aab7c4');
};
$('#id_default_app').change(function () {
    appSelected = $(this).val();
    if (!appSelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});