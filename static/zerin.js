

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
