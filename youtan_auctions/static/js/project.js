/* Project specific Javascript goes here. */

/**
 * Convert date from longdate format to shortdate brazilian format
 * @param {String} date
 * @returns {String}
 */
 const convertDate = (date) => {
    if(!date) return "-"
    // Separates date from time
    let splittedDate = date.split('T');
    daysDate = splittedDate[0];

    timeDate = splittedDate.length > 1 ? splittedDate[1].split('Z')[0].split('.')[0] : '';
    daysDate = daysDate.split('-');
    // Converts date to brazilian format DD/MM/YYYY - hh:mi:ss
    let finalDate = timeDate ? `${daysDate[2]}/${daysDate[1]}/${daysDate[0]} - ${timeDate}` : `${daysDate[2]}/${daysDate[1]}/${daysDate[0]}`;
    return finalDate;
}

const formatDate = (date) => {
    if(!date) return "-"
    // Separates date from time
    let splittedDate = date.split('T');
    daysDate = splittedDate[0];
    daysDate = daysDate.split('-');
    // Converts date to brazilian format DD/MM/YYYY - hh:mi:ss
    return `${daysDate[2]}/${daysDate[1]}/${daysDate[0]}`;
}

// Toggle page loading
const toggleLoading = () => {
    $('#loading').toggleClass('d-none');
}

/**
 * Get the tr data-id from the specified element
 * @param {Element} target - Table row element to get the data-id
 * @param {String} data - Data name to get from tr
 *
 * @returns {String}
 */
const getRowData = (target, data) => {
    return target.closest('tr').data(data);
};

/**
 * Get the tr index from the specified element starting from 0 index (first row)
 * @param {Element} table - DataTable element to get the index from
 * @param {Element} target - Table row element to get the index of
 * @returns {Numeric}
 */
 const getDataTableRowIndex = (table, target) => {
    return table.row( target.closest('tr') ).index();
};

/**
 * Create alert on top-right page
 * @param {String} type - Type of toast. Types alloweds: success, error, warning and info
 * @param {String} msg - Message of toast.
 */
 const createAlert = (type, msg) => {
    if (!["error", "success", "info", "warning"].includes(type)) type = "info";
    toastr.options = {
        "closeButton": true,
        "debug": false,
        "newestOnTop": true,
        "progressBar": true,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    };

    toastr[type](msg);
};

/**
 * Request a method in specified route and, optionally, primary key in the API
 * Data also can be sent together in the request
 * @param {String, String, Integer, Object} target - Method, Route and the Primary Key to get the data of
 * @returns {Object} - Ajax object to be handled with ".done"
 */
 const apiRequest = (method, route, primaryKey = null, data = {}) => {

    var url = `/api/v1/${route}`;
    if (primaryKey) {
        url = `/api/v1/${route}/${primaryKey}`;
    };

    let methodsDescription = {
        'GET': 'buscar',
        'POST': 'criar',
        'PUT': 'atualizar',
        'PATCH': 'atualizar',
        'DELETE': 'deletar'
    }

    let request = {
        url: url,
        method: method,
        error: function (request, status, error) {
            console.log(`Sent data: ${JSON.stringify(data)}`);
            console.log(`Error in ${method} request! URL: ${url}`);
            console.log(request.responseText);

            createAlert('error', `Erro ao ${methodsDescription[method]}`);
        },
    }

    if (method != 'GET') {
        request.data = JSON.stringify(data);
        request.contentType = "application/json";
        request.dataType = "json";

        // Add trailing slash to route if not exists
        if (request.url.slice(-1) != '/') request.url += '/';
    }

    return $.ajax(request);
};

/*
 * Create filter for every datatable columns
 * This function should be called inside the "initComplete" function on the datatable instance
 * @param {Element} table - Table datatable element to create the filter
 */
const columnFilter = (table) => {
    // Adding Search Fields to Columns
    var tableId = $(table).attr('id');
    $(`#${tableId} tfoot th.sort`).each( function () {
        var title = $(this).text();
        $(this).html( `<input type="text" size="10" placeholder="${title}" />` );
    } );
    // Create search event for every column with "sort" class
    table.api().columns('.sort').every(function(){
      var that = this;

      $( 'input', this.footer() ).on( 'keyup change clear', function (){
        if (that.search() !== this.value) {
          that
            .search( this.value )
            .draw();
        }
      } );
    } );
}


/**
 * Disable every button and input in element
 * @param {Element} row
 */
const disableElement = (row) => {
    $(row).find("input,button,textarea,select").attr("disabled", "disabled");
}

/**
 * Update single row in data table and invalidate the row's cache data
 * @param {Element} table - Table datatable element to update the row
 * @param {Numeric} rowIndex
 * @param {Object} data
 */
 const updateRow = (table, rowIndex, data) => table.row(rowIndex).data(data).draw(false);

 /**
  * Remove single row in data table and invalidate the row's cache data
  * @param {Element} table - Table datatable element to remove the row
  * @param {Numeric} rowIndex
  */
 const removeRow = (table, rowIndex) => table.row(rowIndex).remove().draw(false);

 /**
  * Clean all inputs and fields in form element
  * @param {String} form - Form id to clean
  */
const cleanForm = (form) => {
    $(form).find('input, textarea, select').val('').trigger('change');
}

/**
 * Transform object to string list separated by comma using "value" key
 * @param {Object} object
 * @returns {String}
 */
 const objStrList = valuesArr => valuesArr.map(item => item.value).join(",");

/**
 * Set element as Tagify input
 * Reference: https://preview.keenthemes.com/metronic8/demo1/documentation/forms/tagify.html
 * @param {String} selector - Selector of element to set as Tagify
 * @param {Object} custom - Custom options to set
 */
const setTagify = (selector, custom = {originalInputValueFormat: objStrList}) => {
    return new Tagify(document.querySelector(selector), custom);
}

// Convert any string to camel case
const camelize = (str) => {
    return str.normalize("NFD").replace(/\W+(.)/g, function(match, chr)
        {
            return chr.toUpperCase();
        });
}

const currency = (v) => {
    if (v != '') {
        return `R$ ${parseFloat(v).toFixed(2).replace('.', ',')}`;
    } else {
        return `-`;
    }
}


class DomElement {
    constructor(type, args=null) {
        this.type = type;
        this.args = args;
    }

    get() {
        let element = document.createElement(this.type);
        if (this.args != null) {
            for (const [key, value] of Object.entries(this.args)) {
                element[key] = value;
            };
        }
        return element;
    }
}