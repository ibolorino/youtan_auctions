$(document).ready(function(){
    let listUsersUrl = 'http://localhost:8000/api/v1/users/';
    let divUsers = document.getElementById('card_users_list');
    let totalUsers;

    $.ajax({
        url: listUsersUrl,
        method: 'GET',
        success: function(response) {
            totalUsers = response.length;
            if (totalUsers > 0) {
                divUsers.appendChild(usersTable(response));
            } else {
                divUsers.insertAdjacentHTML("beforeend", "<h4>Nenhum Usuário Cadastrado.<h4>");
            }
        },
        error: function(error) {
            console.log(error)
        }
    });

    const usersTable = (users) => {
        const deleteUserCallback = (id, row) => {
            let seleteUserUrl = `http://localhost:8000/api/v1/users/${id}/`
            $.ajax({
                url: seleteUserUrl,
                method: 'DELETE',
                success: function(response) {
                    createAlert('success', `Usuário excluído com sucesso`);
                    row.remove();
                    totalUsers -= 1;
                    if (totalUsers == 0) {
                        divUsers.innerHTML = "<h4>Nenhum Usuário Cadastrado.<h4>";
                    };
                },
                error: function(error) {
                    createAlert('error', `${error.responseText}`);
                }
            });
        }

        let usersTable = new DomElement('table').get();
        usersTable.className = 'table table-striped table-hover gx-5';
        usersTable.innerHTML = `
        <thead>
            <tr class="fw-bolder">
                <th scope="col">Nome</th>
                <th scope="col">Username</th>
                <th scope="col">Email</th>
                <th scope="col">Super usuário</th>
                <th scope="col"></th>
            </tr>
        </thead>
        `;
        let tBody = new DomElement('tbody').get();
        users.map( user => {
            let row = new DomElement('tr').get();
            row.innerHTML = `
                <td>${user.name}</td>
                <td>${user.username}</td>
                <td>${user.email}</td>
                <td>${user.is_staff ? 'Sim' : 'Não'}</td>
            `;
            let cell = new DomElement('td').get();
            cell.insertAdjacentHTML('beforeend', `<a href="/users/${user.id}/update/"><i class="ms-2 fa-regular fa-pen-to-square"></i></a>`);
            let deleteButtonArgs = {
                className: 'ms-2',
                href: '#',
                innerHTML: `<i class="fa-solid fa-trash text-primary"></i>`,
                onclick: function() {deleteUserCallback(user.id, row)}
            };
            let deleteButton = new DomElement('a', deleteButtonArgs).get();
            cell.appendChild(deleteButton);
            row.appendChild(cell);
            tBody.appendChild(row);
        });
        usersTable.appendChild(tBody);
        return usersTable;
    }
});