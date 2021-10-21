var formController = (function(){
    // FORM ELEMENT VALUE SELECTOR
    function selectValue(id) {
        return document.querySelector(id).value;
    }

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
    let gender;
    document.querySelector('#male').addEventListener('click', getGenderValue);
    document.querySelector('#female').addEventListener('click', getGenderValue);

    function getGenderValue(){
        gender = this.value;
    }

    // PORTAL FORM SUBMIT FUNCTION
    $('#portal-form').submit(function(){

        // SELECT INPUT VALUES
        let firstName = selectValue('#first-name');
        let middleName = selectValue('#middle-name');
        let lastName = selectValue('#last-name');
        let email = selectValue('#email');
        let dateOfBirth = selectValue('#date-of-birth');
        let phoneNumber = selectValue('#phone-number');
        let address = selectValue('#address');
        let state = selectValue('#state-select');
        let localGovernment = selectValue('#lga');
        let nextOfKin = selectValue('#nextOfKin');
        let jambScore = selectValue('#jambScore');

        $.ajax({
            url: '/student/add',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify({
                'firstName': firstName,
                'middleName': middleName,
                'lastName': lastName,
                'email': email,
                'dateOfBirth': dateOfBirth,
                'gender': gender,
                'phoneNumber': phoneNumber,
                'address': address,
                'state': state,
                'localGovernment': localGovernment,
                'nextOfKin': nextOfKin,
                'jambScore': jambScore
            }),
            contentType: 'application/json, charset=UTF-8',
            success: function(data) {
                location.reload();
            },
            error: function(err) {
                console.log(err);
            }
        });
    });
})();



    


