$(document).ready(function(){
    let createUserUrl = 'http://localhost:8000/api/v1/users/';
    let userForm = $("#form_create_user");

    userForm.submit(function(e){
        e.preventDefault();
        let formData = $("form").serialize();
        sendForm(formData);
    });
    
    const sendForm = formData => {
        console.log('formData', formData);
        $.ajax({
            url: createUserUrl,
            method: 'POST',
            data: formData,
            dataType: 'json',
            processData: false,
            success: function() {
                createAlert('success', `Usuário criado com sucesso`);
                userForm.trigger("reset");
            },
            error: function(error) {
                if (error.status == 400) {
                    let errors = error.responseJSON;
                    for (const [key, value] of Object.entries(errors)) {
                        createAlert('error', `${key}: ${value[0]}`);
                    }
                } else {
                    createAlert('error', `${error.responseText}`);
                }
            }
        });
    }
});