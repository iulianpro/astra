$("#checkbox_1").click(function () {
    let checked_status = this.checked;
    if (checked_status == true) {
        $("#submit-subscription_1").removeAttr("disabled");
        $("#checkbox_2, #checkbox_3, #checkbox_4, #checkbox_5, #checkbox_6, #checkbox_7, #checkbox_8").attr("disabled", "disabled");
        $('#subscription_choice').text('Abonament 1 luna pe 1 dispozitiv:');
        $("#price_1, #price_2").text('€12.00 / luna');
    } else {
        $("#submit-subscription_1").attr("disabled", "disabled");
        $("#checkbox_2, #checkbox_3, #checkbox_4, #checkbox_5, #checkbox_6, #checkbox_7, #checkbox_8").removeAttr("disabled");
        $('#subscription_choice').text('Selecteaza un abonament:');
        $("#price_1, #price_2").text('€0.00 / luna');
    }
});

$("#checkbox_2").click(function () {
    let checked_status = this.checked;
    if (checked_status == true) {
        $("#submit-subscription_2").removeAttr("disabled");
        $("#checkbox_1, #checkbox_3, #checkbox_4, #checkbox_5, #checkbox_6, #checkbox_7, #checkbox_8").attr("disabled", "disabled");
        $('#subscription_choice').text('Abonament 3 luni pe 1 dispozitiv:');
        $("#price_1, #price_2").text('€25.00 / luna');
    } else {
        $("#submit-subscription_2").attr("disabled", "disabled");
        $("#checkbox_1, #checkbox_3, #checkbox_4, #checkbox_5, #checkbox_6, #checkbox_7, #checkbox_8").removeAttr("disabled");
        $('#subscription_choice').text('Selecteaza un abonament:');
        $("#price_1, #price_2").text('€0.00 / luna');
    }
});

$("#checkbox_3").click(function () {
    let checked_status = this.checked;
    if (checked_status == true) {
        $("#submit-subscription_3").removeAttr("disabled");
        $("#checkbox_2, #checkbox_1, #checkbox_4, #checkbox_5, #checkbox_6, #checkbox_7, #checkbox_8").attr("disabled", "disabled");
        $('#subscription_choice').text('Abonament 6 luni pe 1 dispozitiv:');
        $("#price_1, #price_2").text('€50.00 / luna');
    } else {
        $("#submit-subscription_3").attr("disabled", "disabled");
        $("#checkbox_2, #checkbox_1, #checkbox_4, #checkbox_5, #checkbox_6, #checkbox_7, #checkbox_8").removeAttr("disabled");
        $('#subscription_choice').text('Selecteaza un abonament:');
        $("#price_1, #price_2").text('€0.00 / luna');
    }
});

$("#checkbox_4").click(function () {
    let checked_status = this.checked;
    if (checked_status == true) {
        $("#submit-subscription_4").removeAttr("disabled");
        $("#checkbox_2, #checkbox_3, #checkbox_1, #checkbox_5, #checkbox_6, #checkbox_7, #checkbox_8").attr("disabled", "disabled");
        $('#subscription_choice').text('Abonament 12 luni pe 1 dispozitiv:');
        $("#price_1, #price_2").text('€96.00 / luna');
    } else {
        $("#submit-subscription_4").attr("disabled", "disabled");
        $("#checkbox_2, #checkbox_3, #checkbox_1, #checkbox_5, #checkbox_6, #checkbox_7, #checkbox_8").removeAttr("disabled");
        $('#subscription_choice').text('Selecteaza un abonament:');
        $("#price_1, #price_2").text('€0.00 / luna');
    }
});

$("#checkbox_5").click(function () {
    let checked_status = this.checked;
    if (checked_status == true) {
        $("#submit-subscription_5").removeAttr("disabled");
        $("#checkbox_2, #checkbox_3, #checkbox_4, #checkbox_1, #checkbox_6, #checkbox_7, #checkbox_8").attr("disabled", "disabled");
        $('#subscription_choice').text('Abonament 1 luna pe 2+ dispozitive:');
        $("#price_1, #price_2").text('€15.00 / luna');
    } else {
        $("#submit-subscription_5").attr("disabled", "disabled");
        $("#checkbox_2, #checkbox_3, #checkbox_4, #checkbox_1, #checkbox_6, #checkbox_7, #checkbox_8").removeAttr("disabled");
        $('#subscription_choice').text('Selecteaza un abonament:');
        $("#price_1, #price_2").text('€0.00 / luna');
    }
});

$("#checkbox_6").click(function () {
    let checked_status = this.checked;
    if (checked_status == true) {
        $("#submit-subscription_6").removeAttr("disabled");
        $("#checkbox_2, #checkbox_3, #checkbox_4, #checkbox_5, #checkbox_1, #checkbox_7, #checkbox_8").attr("disabled", "disabled");
        $('#subscription_choice').text('Abonament 3 luni pe 2+ dispozitive:');
        $("#price_1, #price_2").text('€36.00 / luna');
    } else {
        $("#submit-subscription_6").attr("disabled", "disabled");
        $("#checkbox_2, #checkbox_3, #checkbox_4, #checkbox_5, #checkbox_1, #checkbox_7, #checkbox_8").removeAttr("disabled");
        $('#subscription_choice').text('Selecteaza un abonament:');
        $("#price_1, #price_2").text('€0.00 / luna');
    }
});

$("#checkbox_7").click(function () {
    let checked_status = this.checked;
    if (checked_status == true) {
        $("#submit-subscription_7").removeAttr("disabled");
        $("#checkbox_2, #checkbox_3, #checkbox_4, #checkbox_5, #checkbox_6, #checkbox_1, #checkbox_8").attr("disabled", "disabled");
        $('#subscription_choice').text('Abonament 6 luni pe 2+ dispozitive:');
        $("#price_1, #price_2").text('€72.00 / luna');
    } else {
        $("#submit-subscription_7").attr("disabled", "disabled");
        $("#checkbox_2, #checkbox_3, #checkbox_4, #checkbox_5, #checkbox_6, #checkbox_1, #checkbox_8").removeAttr("disabled");
        $('#subscription_choice').text('Selecteaza un abonament:');
        $("#price_1, #price_2").text('€0.00 / luna');
    }
});

$("#checkbox_8").click(function () {
    let checked_status = this.checked;
    if (checked_status == true) {
        $("#submit-subscription_8").removeAttr("disabled");
        $("#checkbox_2, #checkbox_3, #checkbox_4, #checkbox_5, #checkbox_6, #checkbox_7, #checkbox_1").attr("disabled", "disabled");
        $('#subscription_choice').text('Abonament 12 luni pe 2+ dispozitive:');
        $("#price_1, #price_2").text('€120.00 / luna');
    } else {
        $("#submit-subscription_8").attr("disabled", "disabled");
        $("#checkbox_2, #checkbox_3, #checkbox_4, #checkbox_5, #checkbox_6, #checkbox_7, #checkbox_1").removeAttr("disabled");
        $('#subscription_choice').text('Selecteaza un abonament:');
        $("#price_1, #price_2").text('€0.00 / luna');
    }
});

