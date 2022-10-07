$(document).ready(function(){
    let changePasswordUrl = `http://localhost:8000/api/v1/users/${userId}/change_password/`;
    let userForm = $("#form_change_password");

    userForm.submit(function(e){
        e.preventDefault();
        let formData = $("form").serialize();
        sendForm(formData);
    });
    
    const sendForm = formData => {
        $.ajax({
            url: changePasswordUrl,
            method: 'PATCH',
            data: formData,
            dataType: 'json',
            processData: false,
            success: function() {
                createAlert('success', `Senha alterada com sucesso`);
                userForm.trigger("reset");
            },
            error: function(error) {
                if (error.status == 400) {
                    let errors = error.responseJSON;
                    for (const [key, value] of Object.entries(errors)) {
                        createAlert('error', `${key}: ${value[0]}`);
                    }
                }
            }
        });
    }


});