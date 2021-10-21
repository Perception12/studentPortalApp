var formController = (function(){
    var gender;
    // DYNAMIC SELECTION
    document.querySelector('#state-select').addEventListener('change', function(){
        let stateValue = this.value;
        let options = document.querySelector('#lga').children;
        for(let i = 0; i < options.length; i++){
            if(options[i].value == stateValue){
                options[i].style.display = 'block';
            } else{
                options[i].style.display = 'none';
            }
        }
    });

    //GENDER SELECTION
    document.querySelector('#male').addEventListener('click', get_gender);

    document.querySelector('#female').addEventListener('click', get_gender);

    function get_gender(){
        gender = this.value;
        console.log(gender);
    }
})();


// PORTAL FORM SUBMIT FUNCTION

// function selectId(id) {
//     return document.querySelector(id).value;
// }


// function submitForm(){
//     let firstName = selectId('#first-name');
//     let middleName = selectId('#middle-name');
//     let lastName = selectId('#last-name');
//     let email = selectId('#email');
//     let dateOfBirth = selectId('#dateOfBirth');
//     let phoneNumber = selectId('#phone-number');
//     let address = selectId('#address');
//     let state = selectId('#state-select');
//     let localGovernment = selectId('#lga');
//     let nextOfKin = selectId('#nextOfKin');
//     let jambScore = selectId('#jambScore');

//     $.ajax({
//         url: '/student/add',
//         type: 'POST',
//         dataType: 'json',
//         data: JSON.stringify({
//             'firstName': firstName,
//             'middleName': middleName,
//             'lastName': lastName,
//             'email': email,
//             'dateOfBirth': dateOfBirth,
//             'gender': gender,
//             'phoneNumber': phoneNumber,
//             'address': address,
//             'state': state,
//             'localGovernment': localGovernment,
//             'nextOfKin': nextOfKin,
//             'jambScore': jambScore
//         }),
//         contentType: 'application/json, charset=UTF-8',
//         success: function(data) {
//             location.reload();
//         },
//         error: function(err) {
//             console.log(err);
//         }
//     });
// }
