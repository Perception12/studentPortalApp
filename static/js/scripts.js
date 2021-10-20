
// DYNAMIC SELECTION
function stateSelect(){
    var stateValue = document.querySelector('#state-select').value;
    var options = document.querySelector('#lga').children;
    for(let i = 0; i < options.length; i++){
        if(options[i].value == stateValue){
            options[i].style.display = 'block';
        } else{
            options[i].style.display = 'none';
        }
    }
}

