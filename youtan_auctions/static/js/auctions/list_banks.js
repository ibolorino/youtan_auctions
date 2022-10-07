$(document).ready(function(){
    let listBanksUrl = 'http://localhost:8000/api/v1/banks/';
    let divBanks = document.getElementById('card_banks_list');
    let totalBanks;

    $.ajax({
        url: listBanksUrl,
        method: 'GET',
        success: function(response) {
            totalBanks = response.length;
            if (totalBanks > 0) {
                divBanks.appendChild(banksTable(response));
            } else {
                divBanks.insertAdjacentHTML("beforeend", "<h4>Nenhuma Instituição Financeira cadastrada.<h4>");
            }
        },
        error: function(error) {
            console.log(error)
        }
    });

    const banksTable = (banks) => {
        const deleteBankCallback = (id, row) => {
            let delteBankUrl = `http://localhost:8000/api/v1/banks/${id}/`
            $.ajax({
                url: delteBankUrl,
                method: 'DELETE',
                success: function(response) {
                    createAlert('success', `Instituição Financeira excluída com sucesso`);
                    row.remove();
                    totalBanks -= 1;
                    if (totalBanks == 0) {
                        divBanks.innerHTML = "<h4>Nenhuma Instituição Financeira cadastrada.<h4>";
                    };
                },
                error: function(error) {
                    createAlert('error', `${error.responseText}`);
                }
            });
        }

        let banksTable = new DomElement('table').get();
        banksTable.className = 'table table-striped table-hover gx-5';
        banksTable.innerHTML = `
        <thead>
            <tr class="fw-bolder">
                <th scope="col">Nome</th>
                <th scope="col">CNPJ</th>
                ${ isAdmin ? '<th scope="col"></th>' : ''}
            </tr>
        </thead>
        `;
        let tBody = new DomElement('tbody').get();
        banks.map( bank => {
            let row = new DomElement('tr').get();
            row.innerHTML = `
                <td>${bank.name}</td>
                <td>${bank.cnpj}</td>
            `;
            let cell = new DomElement('td').get();
            if (isAdmin) {
                cell.insertAdjacentHTML('beforeend', `<a href="/banks/${bank.id}/update/"><i class="ms-2 fa-regular fa-pen-to-square"></i></a>`);
                let deleteButtonArgs = {
                    className: 'ms-2',
                    href: '#',
                    innerHTML: `<i class="fa-solid fa-trash text-primary"></i>`,
                    onclick: function() {deleteBankCallback(bank.id, row)}
                };
                let deleteButton = new DomElement('a', deleteButtonArgs).get();
                cell.appendChild(deleteButton);
                row.appendChild(cell);
            };
            tBody.appendChild(row);
        });
        banksTable.appendChild(tBody);
        return banksTable;
    }
});