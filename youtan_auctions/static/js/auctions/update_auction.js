$(document).ready(function(){
    let auctionId = $("#submit-button").data("id");
    let updateAuctionUrl = `http://localhost:8000/api/v1/auctions/${auctionId}/`;
    let auctionForm = $("#form_update_auction");

    auctionForm.submit(function(e){
        e.preventDefault();
        let formData = $("form").serialize();
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
                createAlert('success', `Leilão atualizado com sucesso`);
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