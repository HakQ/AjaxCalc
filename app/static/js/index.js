$(document).ready(function() {
    $('#add').click(function() {
        $.ajax({
            url: "/add",
            method: "POST",
            data: $('form').serialize(),
            success: function(d) {
                $('#output').html("RESULT: "+ d['result']);
            }
        });
    });

    $('#subtract').click(function() {
        $.ajax({
            url: "/subtract",
            method: "POST",
            data: $('form').serialize(),
            success: function(d) {
                $('#output').html("RESULT: "+ d['result']);
            }
        });
    });

    $('#multiply').click(function() {
        $.ajax({
            url: "/multiply",
            method: "POST",
            data: $('form').serialize(),
            success: function(d) {
                $('#output').html("RESULT: "+ d['result']);
            }
        });
    });

    $('#divide').click(function() {
        $.ajax({
            url: "/divide",
            method: "POST",
            data: $('form').serialize(),
            success: function(d) {
                $('#output').html("RESULT: "+ d['result']);
            }
        });
    });
})