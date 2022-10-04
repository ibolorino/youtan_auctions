$(document).ready(function(){
    let createAuctionUrl = 'http://localhost:8000/api/v1/auctions/';
    let auctionForm = $("#form_create_auction");

    auctionForm.submit(function(e){
        e.preventDefault();
        let formData = $("form").serialize();
        sendForm(formData);
    });
    
    const sendForm = formData => {
        $.ajax({
            url: createAuctionUrl,
            method: 'POST',
            data: formData,
            dataType: 'json',
            processData: false,
            success: function() {
                createAlert('success', `Leilão criado com sucesso`);
                auctionForm.trigger("reset");
                $('select', auctionForm).trigger("change");
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