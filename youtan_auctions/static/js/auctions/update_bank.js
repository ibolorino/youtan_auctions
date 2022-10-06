$(document).ready(function(){
    let bankId = $("#submit-button").data("id");
    let updateBankUrl = `http://localhost:8000/api/v1/banks/${bankId}/`;
    let bankForm = $("#form_update_bank");

    bankForm.submit(function(e){
        e.preventDefault();
        let formData = $("form").serialize();
        sendForm(formData);
    });
    
    const sendForm = formData => {
        $.ajax({
            url: updateBankUrl,
            method: 'PATCH',
            data: formData,
            dataType: 'json',
            processData: false,
            success: function() {
                createAlert('success', `Instituição Financeira atualizada com sucesso`);
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