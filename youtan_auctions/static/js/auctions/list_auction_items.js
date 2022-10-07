$(document).ready(function(){
    let listPropertiesUrl = `http://localhost:8000/api/v1/properties/?auction_id=${auctionId}`;
    let listVehiclesUrl = `http://localhost:8000/api/v1/vehicles/?auction_id=${auctionId}`;
    let divItems = document.getElementById('card_items_list');
    let properties, vehicles;


    $.when(
        $.get(listPropertiesUrl),
        $.get(listVehiclesUrl),
    ).then(function(properties_items, vehicles_items) {
        if (properties_items[1] == "success") {
            properties = properties_items[0];
        };
        if (vehicles_items[1] == "success") {
            vehicles = vehicles_items[0];
        };
        getItemsCards(properties, vehicles);
    });

    const getItemsCards = (properties, vehicles) => {
        if (properties.length > 0) {
            properties.map(
                property => {
                    divItems.appendChild(itemElement(property, "property"));
                }
            );
        };
        if (vehicles.length > 0) {
            vehicles.map(
                vehicle => {
                    divItems.appendChild(itemElement(vehicle, "vehicle"));
                }
            );
        };
        if (properties.length + vehicles.length == 0) divItems.innerHTML = "<h4>Nenhum item cadastrado.</h4>"
    };


    const itemElement = (item, itemType) => {
        let itemCard = document.createElement('div');
        itemCard.className = 'card p-3 m-3 card-item';
        itemCard.style.cssText += 'width: 200px;';
        itemCard.id = `${itemType}-${item.id}`;
        itemCard.appendChild(itemHeader());
        itemCard.appendChild(itemBody());
        return itemCard;

        function itemHeader() {
            let itemHeader = document.createElement('div');
            itemHeader.className = 'card-header';
            itemHeader.innerHTML = `<h3 class="card-title">${item.name}</h3>`;
            return itemHeader;
        }

        function itemBody() {
            let itemBody = document.createElement('div');
            let currentBid = item.bids.length > 0 ? item.bids[0].value : item.initial_bid;
            if (item.images.length > 0) {
                let divImgAttrs = {
                    innerHTML: `<img src="${item.images[0].image}" style="width:100%">`,
                    onclick: function() {setImagesModal(item)}
                }
                let divImg = new DomElement('div', divImgAttrs).get();
                divImg.style.cssText += 'cursor: pointer;';
                itemBody.appendChild(divImg);
            }
            itemBody.className = 'card-body px-1';
            itemBody.insertAdjacentHTML('beforeend', `
                <div>
                    <p class="mb-0"><b>Lance inicial: </b>${currency(item.initial_bid)}</p>
                    <p class="mb-0"><b>Incremento: </b>${currency(item.minimum_increment)}</p>
                    <h6 class="mb-0 mt-3"><b>Lance atual: </b>${currency(currentBid)}</h6>
                </div>
            `);
            itemBody.appendChild(itemActions())
            return itemBody;
        };

        function itemActions() {
            const viewBidCallback = e => {
                e.preventDefault();
                setViewBidsModal(item);
            };

            const bidCallback = e => {
                e.preventDefault();
                setBidModal(item, itemType);
            };

            let itemActions = document.createElement('div');

            let viewBids = document.createElement('a');
            viewBids.href = '#';
            viewBids.className = 'btn btn-secondary btn-sm mb-1 mt-3 w-100';
            viewBids.innerHTML = 'Ver Lances';
            viewBids.onclick = viewBidCallback;

            let bid = document.createElement('a');
            bid.href = '#';
            bid.className = 'btn btn-primary btn-sm w-100';
            bid.innerHTML = 'Dar Lance';
            bid.onclick = bidCallback;


            itemActions.appendChild(viewBids);
            itemActions.appendChild(bid);

            return itemActions;
        };

        function setViewBidsModal(item) {
            let btnSave = document.getElementById('btn-save-bid');
            if (btnSave) btnSave.remove();

            $("#modal-title").html(item.name);
            bids = "<h4>Nenhum lance efetuado.</h4>";
            if (item.bids.length > 0) {
                let bid_rows = '';    
                item.bids.map( bid => {
                    bid_rows += `
                        <tr>
                            <td>${convertDate(bid.date)}</td>
                            <td>${currency(bid.value)}</td>
                            <td>${bid.user}</td>
                        </tr>
                    `
                });
                bids = `
                    <table class="table table-striped table-hover gx-5">
                        <thead>
                            <tr class="fw-bolder">
                                <th scope="col">Data</th>
                                <th scope="col">Valor</th>
                                <th scope="col">Usuário</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${bid_rows}
                        </tbody>
                `
            };
            $("#modal-body").html(bids);
            $("#item-bid-modal").modal("show");
        };

        function setBidModal(item, itemType) {
            const sendBid = e => {
                let data = {
                    "value": input.value,
                }
                data[itemType] = item.id;
                $.ajax({
                    url: `http://localhost:8000/api/v1/bid/${itemType}/`,
                    method: 'POST',
                    data: data,
                    dataType: 'json',
                    success: function() {
                        createAlert('success', `Lance enviado com sucesso`);
                        $("#item-bid-modal").modal("hide");
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

            $("#modal-title").html(item.name);
            let modalBody = document.getElementById('modal-body');
            let modalFooter = document.getElementById('modal-footer');

            let btnSave = document.getElementById('btn-save-bid');
            if (btnSave) btnSave.remove();

            modalBody.innerHTML = '<label for="value" class="form-label">Valor do lance</label>';

            let input = document.createElement('input');
            input.type = 'number';
            input.className = 'form-control';
            input.id = 'value';
            input.name = 'value';
            modalBody.appendChild(input);

            btnSave = document.createElement('button');
            btnSave.id = 'btn-save-bid';
            btnSave.className = 'btn btn-primary';
            btnSave.innerHTML = 'Salvar';
            btnSave.onclick = sendBid;
            modalFooter.appendChild(btnSave);

            $("#item-bid-modal").modal("show");
        };

        function setImagesModal(item) {
            let btnSave = document.getElementById('btn-save-bid');
            if (btnSave) btnSave.remove();
            $("#modal-title").html(item.name);
            let carouselIndicators = '';
            let carouselImages = '';
            item.images.forEach(function (image, i) {
                carouselIndicators += `<li data-bs-target="#kt_carousel_1_carousel" data-bs-slide-to="${i}" class="ms-1 ${i==0 ? ' active' : '' }"></li>`;
                carouselImages += `
                <div class="carousel-item ${i==0 ? ' active' : '' }" style="max-height: 100%">
                    <img src="${image.image}" style="max-height: 100%; max-width: 100%">
                </div>
                `
            });
            let modalBody = `
            <div id="kt_carousel_1_carousel" class="carousel carousel-custom slide" data-bs-ride="carousel" data-bs-interval="8000">
                <div class="d-flex align-items-center justify-content-between flex-wrap">
                    <span class="fs-4 fw-bold pe-2"></span>
                    <ol class="p-0 m-0 carousel-indicators carousel-indicators-dots">
                        ${carouselIndicators}
                    </ol>
                </div>
                <div class="carousel-inner pt-8">
                    ${carouselImages}
                </div>
            </div>
            `;
            $("#modal-body").html(modalBody);
            $("#item-bid-modal").modal("show");
        }
    }




});