$(document).ready(function(){
    let createAuctionUrl = 'http://localhost:8000/api/v1/properties/';
    let auctionForm = $("#form_create_property");

    auctionForm.submit(function(e){
        e.preventDefault();
        let formData = new FormData($("form").get(0));
        sendForm(formData);
    });
    
    const sendForm = formData => {
        $.ajax({
            url: createAuctionUrl,
            method: 'POST',
            data: formData,
            cache: false,
            dataType: 'json',
            processData: false,
            contentType: false,
            success: function(response) {
                console.log(response);
                createAlert('success', `Propriedade criado com sucesso`);
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