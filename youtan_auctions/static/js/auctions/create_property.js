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
                uploadImages(formData, response.id);
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

    function uploadImages(formData, id) {
        let imgUrl = 'http://localhost:8000/api/v1/properties_images/'
        formData.getAll('images').map( image => {
            let data = new FormData();
            data.append("image", image);
            data.append("property", id);
            $.ajax({
                url: imgUrl,
                method: 'POST',
                data: data,
                processData: false,
                contentType: false,
                success: function() {
                    createAlert('success', `Imagem associada com sucesso`);
                },
                error: function(error) {
                    createAlert('error', `${error.responseText}`);
                }
            })
        });
    }


});