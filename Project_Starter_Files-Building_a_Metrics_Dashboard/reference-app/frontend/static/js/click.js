$(document).ready(function () {

    // Trigger backend via /api
    $("#firstbutton").click(function () {
        $.ajax({
            url: "/api", 
            success: function (result) {
                $("#firstbutton").toggleClass("btn-primary:focus");
            }
        });
    });

    // Trigger trial-service via /trace
    $("#secondbutton").click(function () {
        $.ajax({
            url: "/trace",
            success: function (result) {
                $("#secondbutton").toggleClass("btn-primary:focus");
            }
        });
    });
});
