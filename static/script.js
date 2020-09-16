/*message will disappear after few seconds*/
$(document).ready(function(){
    $(".flash").delay(2000).slideUp(300);
});

/*add checked to the first radio button of each form in the survey*/
if($('form input[type="radio"]').length){
    $('form input[type="radio"]')[0].checked = true;
}