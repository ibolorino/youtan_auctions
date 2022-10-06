$(document).ready(function(){
    let itemId = $("#submit-button").data("id");
    let updateAuctionUrl = `http://localhost:8000/api/v1/${itemType}/${itemId}/`;
    let itemForm = $("#form_update_item");
    let totalImages = document.getElementById('tbody_images').children.length;
    let divImages = document.getElementById('div_photos');

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
    };

    $(".btn-del-img").click(function(e) {
        e.preventDefault();
        let btnDel = $(this);
        let row = btnDel.closest('tr').get(0);
        let id = btnDel.data('id');
        deleteImage(id, row);
    });

    const deleteImage = (id, row) => {
        let url = `http://localhost:8000/api/v1/${itemType}_images/${id}/`;
        $.ajax({
            url: url,
            method: 'DELETE',
            success: function(response) {
                createAlert('success', `Foto excluída com sucesso`);
                row.remove();
                totalImages -= 1;
                if (totalImages == 0) {
                    divImages.innerHTML = "<h4>Nenhuma foto cadastrada.<h4>";
                };
            },
            error: function(error) {
                createAlert('error', `${error.responseText}`);
            }
        });
    }
});