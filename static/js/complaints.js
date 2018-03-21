// $(document).ready(function() {
//     $('#submit_complaint').onclick(function() {
//         console.log('YES');
//         console.log($(this).serializeArray());
//             // $('#progress').css('display','block');
//             $.ajax({
//                 data: $(this).serializeArray(),
//                 type: "GET",
//                 url: "ajax/submit_complaints/",
//                 success: function(response) {
//                     console.log('response = ', response);
//                     Materialize.toast('Successfully Changed!', 4000);
//                 }
//             });
//             return false;
//         });
// });

$(document).ready(function() {

    $('#submit_complaint').submit(function() {
        console.log('YESS');
            // $('#progress').css('display','block');
            $.ajax({
                data: $(this).serializeArray(),
                type: "POST",
                url: "ajax/submit_complaints/",
                success: function(response) {
                    console.log(response);
                    if(response['status'] === true) {
                        window.location.href = '/complaints/success';
                    } else {
                        Materialize.toast(response['message'], 4000);
                        console.log('Error');
                    }
                },
                error: function() {
                    console.log('Error, Please refresh this page');
                    Materialize.toast('There is some error with website. Please contact Admin', 4000);
                }
            });
            return false;
        });

});

$(document).ready(function() {
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
               'Threat': null
           },
           limit: Infinity,
           minLength: 1
       }
    });
    $('.chips').on('chip.add', function(e, chip){
        var val = $('input[name=complaint_tag]').val();
        if(val.length !== 0) {
            val += ', ';
        }
        $('input[name=complaint_tag]').val(val + chip['tag']);
        console.log('Final valll = ', $('input[name=complaint_tag]').val());
    });

    $('.chips').on('chip.delete', function(e, chip){
        var val = $('input[name=complaint_tag]').val();
        console.log('replacing = ', chip['tag']);
        if(val.indexOf(',') === -1) {
            $('input[name=complaint_tag]').val(val.replace(chip['tag'], ''));
        } else {
            $('input[name=complaint_tag]').val(val.replace(chip['tag']+', ', ''));
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