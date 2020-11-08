
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
if (appSelected != '') {
    $('#id_app').css('color', '#000');
} else {
    $('#id_app').css('color', '#aab7c4');
};
$('#id_app').change(function () {
    appSelected = $(this).val();
    if (appSelected != '') {
        $(this).css('color', '#000');
    } else {
        $(this).css('color', '#aab7c4');
    }
});

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
});

$(document).ready(function () {
    $('#submit-button').click(function (e) {
        $('#d-loading-overlay').removeClass('d-none');
    });
});
