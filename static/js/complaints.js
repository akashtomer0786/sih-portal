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
    $('select').material_select();
    $('.chips').material_chip();
    // $('.chips-autocomplete').material_chip({
    //     secondaryPlaceholder: 'Test',
    //     placeholder: 'Hello',
    //    autocompleteData: {
    //        data: {
    //            'Apple': null,
    //            'Microsoft': null,
    //            'Google': null
    //        },
    //        limit: Infinity,
    //        minLength: 1
    //    }
    // });
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