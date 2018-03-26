// https://stackoverflow.com/questions/8888491/how-do-you-display-javascript-datetime-in-12-hour-am-pm-format
function formatAMPM(date) {
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? 'pm' : 'am';
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? '0'+minutes : minutes;
  return hours + ':' + minutes + ' ' + ampm;
}

$(document).ready(function () {
    localStorage.setItem('limit', 1);

    $('#submit_complaint').submit(function () {
        console.log('YESS');
        // $('#progress').css('display','block');
        $.ajax({
            data: $(this).serializeArray(),
            type: "POST",
            url: "ajax/submit_complaints/",
            success: function (response) {
                console.log(response);
                if (response['status'] === true) {
                    window.location.href = '/complaints/success';
                } else {
                    Materialize.toast(response['message'], 4000);
                    console.log('Error');
                }
            },
            error: function () {
                console.log('Error, Please refresh this page');
                Materialize.toast('There is some error with website. Please contact Admin', 4000);
            }
        });
        return false;
    });

    // TODO: Add Animation like Fade in for each request
    $('#get_complaints').click(function () {
        localStorage.setItem('limit', parseInt(localStorage.getItem('limit')) + 1);
        console.log(localStorage.getItem('limit'));
        $.ajax({
            type: "GET",
            url: "ajax/get_complaints?limit=" + localStorage.getItem('limit'),
            success: function (response) {
                if (response['result'] === true) {
                    var complaint_body = document.getElementById('complaint_body');
                    for (i = 0; i < response['complaints'].length; i++) {
                        var complaint_date = new Date(response["complaints"][i]["complaint_date"]);
                        var tags_string = '';
                        var tags_list = response['complaints'][i]['complaint_tag'].split(',');
                        for (j = 0; j < tags_list.length; j++) {
                            tags_string += '<div class="chip">\n' +
                                tags_list[j] + '\n' +
                                '</div>\n';
                        }
                        complaint_body.innerHTML += '<div class="card white">\n' +
                            '<div class="card-content">\n' +
                            '<p><a href="/complaints/details/{{ complaint.id }}"\n' +
                            'class="card-title black-text">' + response["complaints"][i]["subject"] + '</a>\n' +
                            '</p>\n' +
                            '</div>\n' +
                            '<div class="card-action">\n' +
                            '<span>\n' +
                            tags_string +
                            '</span>\n' +
                            '<span class="" style="float: right;">' + complaint_date.toDateString() + ', ' + formatAMPM(complaint_date) + '</span>\n' +
                            '</div>\n' +
                            '</div>';
                    }
                } else {
                    Materialize.toast('There is some error with request, Please refresh', 4000);
                }
            },
            error: function () {
                console.log('Error, Please refresh this page');
                Materialize.toast('There is some error with website. Please contact Admin', 4000);
            }
        });
        return false;
    });

});

$(document).ready(function () {
    $('#id_complaint_tag').val('');
    console.log('RAN');
    $('select').material_select();
    $('input.tag-autocomplete').autocomplete({
        data: {
            "Apple": null,
            "Microsoft": null,
            "Google": null
        },
        limit: 20,
        onAutocomplete: function (val) {
            console.log('It is working = ', val);
            $("#id_complaint_tag").val("WOW");
        },
        minLength: 1
    });
    $('.chips').material_chip();
    $('.chips-autocomplete').material_chip({
        autocompleteOptions: {
            data: {
                'Phishing': null,
                'Cyber Stalking': null,
                'Exclusion': null,
                'Fake Profile': null,
                'Frapping': null,
                'Harrassment': null,
                'Outing': null,
                'Trickery': null,
                'Trolling': null,
                'Pornography': null,
                'Nudity': null,
                'Threat': null,
                'Flaming': null,
                'Denigration': null,
                'Impersonation': null
            },
            limit: Infinity,
            minLength: 1
        }
    });
    $('.chips').on('chip.add', function (e, chip) {
        var val = $('input[name=complaint_tag]').val();
        if (val.length !== 0) {
            val += ',';
        }
        $('input[name=complaint_tag]').val(val + chip['tag']);
        console.log('Final valll = ', $('input[name=complaint_tag]').val());
    });

    $('.chips').on('chip.delete', function (e, chip) {
        var val = $('input[name=complaint_tag]').val();
        console.log('replacing = ', chip['tag']);
        if (val.indexOf(',') === -1) {
            $('input[name=complaint_tag]').val(val.replace(chip['tag'], ''));
        } else {
            $('input[name=complaint_tag]').val(val.replace(chip['tag'] + ',', ''));
        }
    });
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 100, // Creates a dropdown of 100 years to control year,
        format: 'mm/dd/yyyy',
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        min: new Date(1957, 1, 1),
        max: new Date(2018, 1, 1),
        closeOnSelect: false // Close upon selecting a date,
    });
});