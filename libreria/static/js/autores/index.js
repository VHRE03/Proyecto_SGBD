function listar_usuarios() {
    $.ajax({
        url: "autores",
        type: "get",
        dataType: "json",
        success: function(response) {
            console.log(response)   
        }
    })
}

$(document).ready(function () {
    listar_usuarios()
})