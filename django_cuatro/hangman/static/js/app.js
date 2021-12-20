// READY
// DEFINICION DE DOM ID
// ACTIONS
// SERVICE

$(document).ready(PageReady);

function PageReady() {
    console.log('hola PageReady')
      $(`#${DOM_IDS.BUTTON_SAVE}`).on('click', listenButton);

}

var DOM_IDS = {
    BUTTON_SAVE: 'button-save',
    INPUT_VALUE: "input-value-1",
}

function listenButton(){
    var value = $(`#${DOM_IDS.INPUT_VALUE}`).val();
    console.log('this is the value: '+value)
    triggerGameTurn(1, value, triggerGameTurnSuccess, triggerGameTurnError )
}

function triggerGameTurnSuccess() {
    console.log('triggerGameTurnSuccess')
}


function triggerGameTurnError() {
    console.log('triggerGameTurnSuccess')
}

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