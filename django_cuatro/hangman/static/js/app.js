// READY 
// DEFINICION DE DOM ID 
// ACTIONS
// SERVICE

$(document).ready(PageReady);

function PageReady() {
    console.log('hola PageReady')
}



console.log('hola app')

// SERVICE

function triggerGameTurn(id, char, successCallback, errorCallback) {
    data = {
        'id': id,
        'choise': char
    }
    $.ajax({
        contentType: 'application/json;charset=UTF-8',
        // headers: {
        // "Authorization": `Bearer ${token}`,
        // },
        data: JSON.stringify(data),
        error: errorCallback,
        success: successCallback,
        type: 'POST',
        url: `game_turn`,
    })
}