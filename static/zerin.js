var ALLCONTACTS_GROUP = -1;

var alertInterval;

SUCCESS = 'success'
INFO = 'info'
WARNING = 'warning'
ERROR = 'error'

function display_alert(level, message, delay) {
    // level: success, info, warning, error

    // guess delay type
    if (delay == undefined)
        delay = 1000;

    if (delay < 100)
        delay = delay * 1000;

    if (level == ERROR && delay < 4000)
        delay = 4000;

    var alertbox = $("<div id='alertbox' class='alert alert-"+ level +"'><p>"+ message +"</p></div>");
    $(alertbox).prependTo($("#main"));

    function remove_alert() {
        clearInterval(alertInterval);
        $("#alertbox").fadeOut('slow', function() {$("#alertbox").remove();});
    }

    var alertInterval = setInterval(remove_alert, delay);
}

function addJQ_addressbook_group_list() {
    $.getJSON('/addressbook/group_list', function(data) {
        $.each(data.groups, function(num, group) {
            row = "<li class='droppable'><a href='#' group_id=" + group.id +">" + group.display_name + "</a></li>";
            $("#groups").append(row);
          });
        addJQ_addressbook_contact_list();
        load_contact_list_from_group_id(ALLCONTACTS_GROUP);

        $("#groups li").droppable({
            activeClass: "ui-state-hover",
            hoverClass: "ui-state-active",
            tolerance:'pointer',
            drop: function( event, ui ) { 
                var contact_id = ui.draggable.attr('contact_id');
                var group_id = $(this).children("a").attr('group_id');
                if (contact_id == undefined || group_id == undefined)
                    return false;
                $.getJSON('/addressbook/add_contact/'+ contact_id +'/to_group/' + group_id, function(data){
                    display_alert(data.return, data.return_html, 2);
                });
            },
        });
    });
}

function load_contact_list_from_group_id(group_id) {
    var group_link = $("#groups li a[group_id="+group_id+"]");
    $(group_link).parent().parent().children('li').not($(group_link).parent()).removeClass('active');
    $(group_link).parent().addClass('active');

    $.getJSON('/addressbook/contact_for/' + group_id, function(data) {
        $("#contacts_table").empty();
        $.each(data.contacts, function(num, contact) {
            row = "<tr><td class='td-icon'><i class='icon-user' contact_id=" + contact.id +"/></td><td class='td-link' contact_id=" + contact.id +">" + contact.display_name + "</td></tr>";
            $("#contacts_table").append(row);
        });

        $("#contacts_table td.td-icon i").draggable({
            revert: "invalid",
            containment: $("#main"),
            helper: function (event) { return $("<button class='btn btn-small' type='button'><i class='icon-user'></i> "+ $(this).parent().parent().children("td.td-link").html() +"</button>")},
            cursor: "move"
        });

        addJQ_addressbook_contact_info();
    });
}

function addJQ_addressbook_contact_list() {
    $("#groups li a").click(function() {
        group_id = $(this).attr('group_id');
        load_contact_list_from_group_id(group_id);
    });
}

function addJQ_addressbook_contact_info() {
     $("#contacts_table td.td-link").click(function() {
        contact_id = $(this).attr('contact_id');
        $.getJSON('/addressbook/contact/' + contact_id, function(data) {
            $("#contact_info h2").html(data.contact.display_name);
            var edit_field = $("#contact_info input#edit_contact_name");
            edit_field.attr('value', data.contact.display_name);
            $("#contact_info ul").empty();
            $.each(data.contact.numbers, function(num, phonenum) {
                row = "<li>" + phonenum.display_number + ' (' + phonenum.operator.display_name + ')' + "</li>";
                $("#contact_info ul").append(row);
            });
            add_JQ_addressbook_contact_fields_edit();
        });

        $.getJSON('/addressbook/transfer_for/' + contact_id, function(data) {
            $("#transfer").empty();
            $.each(data.transfers, function(num, transfer) {
                row = "<tr><td>" + transfer.number.display_number + "</td><td>"+transfer.display_date+"</td><td>"+transfer.amount + " FCFA" + "</td></tr>";
                $("#transfer").append(row);
            });
        });
    });
}

function add_JQ_addressbook_contact_fields_edit() {
    $("#contact_info h2").dblclick(function() {
        $("input#edit_contact_name").toggle();
        $(this).toggle();
    });
}
