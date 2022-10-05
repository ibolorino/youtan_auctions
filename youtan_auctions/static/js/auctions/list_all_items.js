$(document).ready(function(){
    let listPropertiesUrl = 'http://localhost:8000/api/v1/properties/';
    let listVehiclesUrl = 'http://localhost:8000/api/v1/vehicles/';
    let divItems = document.getElementById('card_items_list');
    let totalItems;

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
        totalItems = properties.length + vehicles.length;
        divItems.appendChild(itemsTable(properties, vehicles));
    });

    const itemsTable = (properties, vehicles) => {
        const deleteItemCallback = (id, type, row) => {
            let deleteItemUrl = `http://localhost:8000/api/v1/${type}/${id}`
            $.ajax({
                url: deleteItemUrl,
                method: 'DELETE',
                success: function(response) {
                    createAlert('success', `Item excluído com sucesso`);
                    row.remove();
                    totalItems -= 1;
                    if (totalItems == 0) {
                        divItems.innerHTML = "<h4>Nenhum item cadastrado.<h4>";
                    };
                },
                error: function(error) {
                    createAlert('error', `${error.responseText}`);
                }
            });
        }

        let args = {
            className: 'table table-striped table-hover gx-5',
            innerHTML: `<thead><tr class="fw-bolder">
                <th scope="col">Tipo</th>
                <th scope="col">Nome</th>
                <th scope="col">Leilão 2</th>
                <th scope="col">Lance inicial</th>
                <th scope="col">Último lance</th>
                <th scope="col"></th>
            </tr></thead>`
        };
        if (totalItems == 0) args.innerHTML = '<h4>Nenhum item cadastrado.<h4>';
        let itemsTable = new DomElement('table', args).get();
        let tBody = new DomElement('tbody').get();

        properties.map( property => {
            let row = new DomElement('tr').get();
            row.innerHTML = `
                <td>Imóvel</td>
                <td>${property.name}</td>
                <td>${property.auction.name}</td>
                <td>${currency(property.initial_bid)}</td>
                <td>${property.bids.length > 0 ? currency(property.bids[0].value) : currency(property.initial_bid)}</td>
            `;
            let cell = new DomElement('td').get();
            cell.innerHTML = `<a href="/properties/${property.id}/" id="edit-item-btn""><i class="fa-solid fa-magnifying-glass"></i></a>`;
            if (isAdmin) {
                cell.insertAdjacentHTML('beforeend', `<a href="/properties/${property.id}/update/" id="edit-item-btn""><i class="ms-2 fa-regular fa-pen-to-square"></i></a>`);
                let deleteButtonArgs = {
                    className: 'ms-2',
                    href: '#',
                    innerHTML: `<i class="fa-solid fa-trash text-primary" data-id="${property.id}" data-type="property"></i>`,
                    onclick: function() {deleteItemCallback(property.id, 'properties', row)}
                };
                let deleteButton = new DomElement('a', deleteButtonArgs).get();
                cell.appendChild(deleteButton);
            }
            row.appendChild(cell);
            tBody.appendChild(row);
        });

        vehicles.map( vehicle => {
            let row = new DomElement('tr').get();
            row.innerHTML = `
                <td>Veículo</td>
                <td>${vehicle.name}</td>
                <td>${vehicle.auction.name}</td>
                <td>${currency(vehicle.initial_bid)}</td>
                <td>${vehicle.bids.length > 0 ? currency(vehicle.bids[0].value) : currency(vehicle.initial_bid)}</td>
            `;
            let cell = new DomElement('td').get();
            cell.innerHTML = `<a href="/vehicles/${vehicle.id}/" id="edit-item-btn""><i class="fa-solid fa-magnifying-glass"></i></a>`;
            if (isAdmin) {
                cell.insertAdjacentHTML('beforeend', `<a href="/vehicles/${vehicle.id}/update/" id="edit-item-btn""><i class="ms-2 fa-regular fa-pen-to-square"></i></a>`);
                let deleteButtonArgs = {
                    className: 'ms-2',
                    href: '#',
                    innerHTML: `<i class="fa-solid fa-trash text-primary" data-id="${vehicle.id}" data-type="property"></i>`,
                    onclick: function() {deleteItemCallback(vehicle.id, 'vehicles', row)}
                };
                let deleteButton = new DomElement('a', deleteButtonArgs).get();
                cell.appendChild(deleteButton);
            }
            row.appendChild(cell);
            tBody.appendChild(row);
            tBody.appendChild(row);
        });

        itemsTable.appendChild(tBody);
        return itemsTable;
    }


});