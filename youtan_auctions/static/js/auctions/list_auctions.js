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
            if (isAdmin) auctionHeader.appendChild(adminControls());
            return auctionHeader;
        }

        function auctionBody() {
            let auctionBody = document.createElement('div');
            auctionBody.className = 'card-body pt-5 p-3';
            auctionBody.innerHTML = `
                <h6 class="mb-0"><b>Data final</b></h6>
                <p class="mb-3 lh-sm">${convertDate(auction.date)}</p>
                <h6 class="mb-0"><b>Endereço</b></h6>
                <p class="mb-3 lh-sm">
                    ${auction.address}<br>
                    ${auction.city} - ${auction.state}
                </p>
                <h6 class="mb-0"><b>Instituição Financeira</b></h6>
                <p class="mb-3 lh-sm">
                    ${auction.bank.name}<br>
                    CNPJ ${auction.bank.cnpj}
                </p>
                <a href="/auctions/${auction.id}/items/" class="btn btn-sm w-100 btn-primary mt-3">Ver Items</a>
                `;
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

});