$(document).ready(function(){
    let listAuctionsUrl = 'http://localhost:8000/api/v1/auctions/';
    let divAuctions = document.getElementById('card_auctions_list');
    let totalAuctions;

    $.ajax({
        url: listAuctionsUrl,
        method: 'GET',
        success: function(response) {
            getAuctionsCards(response);
            totalAuctions = response.length;
        },
        error: function(error) {
            console.log(error)
        }
    });

    const getAuctionsCards = auctions => {
        
        let auctionCards = "";
        if (auctions.length > 0) {
            auctions.map(
                auction => {
                    //auctionCards += auctionElement(auction);
                    divAuctions.appendChild(auctionElement(auction));
                }
            );
        } else {
            divAuctions.insertAdjacentHTML("beforeend", "<h4>Nenhum leilão aberto.<h4>");
        }
    };

    const auctionElement = (auction) => {
        let auctionCard = document.createElement('div');
        auctionCard.className = 'card p-3 m-3 card-auction';
        auctionCard.style.cssText += 'width: 200px;';
        auctionCard.id = `auction-${auction.id}`
        auctionCard.appendChild(auctionHeader());
        auctionCard.appendChild(auctionBody());
        return auctionCard;

        function auctionHeader() {
            let auctionHeader = document.createElement('div');
            auctionHeader.className = 'card-header';
            auctionHeader.innerHTML = `<h3 class="card-title">${auction.name}</h3>`;
            auctionHeader.appendChild(adminControls());
            return auctionHeader;
        }

        function auctionBody() {
            let auctionBody = document.createElement('div');
            auctionBody.className = 'card-body';
            auctionBody.innerHTML = `<p><b>Data final: </b>${convertDate(auction.date)}</p>
            <a href="#" class="btn btn-sm w-100 btn-primary">Ver Items</a>`;
            return auctionBody;
        }

        function adminControls() {
            let adminControls = document.createElement('div');
            adminControls.style.cssText += 'position: absolute; right: 10px';
            adminControls.innerHTML = `<a href="/auctions/${auction.id}/update/" id="edit-auction-btn""><i class="fa-regular fa-pen-to-square text-primary"></i></a>`;
            adminControls.appendChild(deleteButton());
            return adminControls;
        };


        function deleteButton() {
            const deleteCallback = (e) => {
                e.preventDefault();
                let id = e.target.dataset.id;
                let deleteAuctionUrl = `${listAuctionsUrl}${id}`
                let auctionCard = document.getElementById(`auction-${id}`);
                $.ajax({
                    url: deleteAuctionUrl,
                    method: 'DELETE',
                    success: function(response) {
                        createAlert('success', `Leilão excluído com sucesso`);
                        auctionCard.remove();
                        totalAuctions -= 1;
                        if (totalAuctions == 0) {
                            divAuctions.insertAdjacentHTML("beforeend", "<h4>Nenhum leilão aberto.<h4>");
                        };
                    },
                    error: function(error) {
                        createAlert('error', `${error.responseText}`);
                    }
                });
            }

            let deleteButton = document.createElement('a');
            deleteButton.id = 'delete-auction-btn';
            deleteButton.href = '#';
            deleteButton.className = "ms-1"
            deleteButton.innerHTML = `<i class="fa-solid fa-trash text-primary" data-id="${auction.id}"></i>`;
            deleteButton.onclick = deleteCallback;
            return deleteButton;
        };


    };

    const getAdminControls = (id) => {
        let adminControls = '';
        if (isAdmin == true) {
            adminControls = `
            <a href="/auctions/${id}/update/" id="edit-auction-btn""><i class="fa-regular fa-pen-to-square text-primary"></i></a>
            <a href="#" onclick="myFunction()" id="delete-auction-btn" data-id="${id}"><i class="fa-solid fa-trash text-primary"></i></a>
            `
        };
        return adminControls;
    };

    function myFunction() {
        console.log("clickou")
    }

    $("#edit-auction-btn").click(function(){
        console.log("click")
    })

});