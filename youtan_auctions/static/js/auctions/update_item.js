$(document).ready(function(){
    let itemId = $("#submit-button").data("id");
    let updateAuctionUrl = `http://localhost:8000/api/v1/${itemType}/${itemId}/`;
    let itemForm = $("#form_update_item");

    itemForm.submit(function(e){
        e.preventDefault();
        let formData = itemForm.serialize();
        sendForm(formData);
    });
    
    const sendForm = formData => {
        $.ajax({
            url: updateAuctionUrl,
            method: 'PATCH',
            data: formData,
            dataType: 'json',
            processData: false,
            success: function() {
                createAlert('success', `Item atualizado com sucesso`);
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