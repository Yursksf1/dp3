
var DOM_IDS = {
    ID_BOTON_AGREGAR: 'boton_agregar_tabla',
    ID_FORMULARIO_OCULTO: 'formulario_oculto',
    ID_GUARDAR_FORMULARIO_OCULTO: 'guardar_form_uno',
    INPUT_NAME: 'input-name',
    ID_REFERENCIA: 'id_referencia'
}

$(document).ready(PageReady);
function PageReady() {
    $(`#${DOM_IDS.ID_BOTON_AGREGAR}`).on("click", showFormTablaUno);
    $(`#${DOM_IDS.ID_GUARDAR_FORMULARIO_OCULTO}`).on("click", guardarFormUno);
}

function showFormTablaUno() {
    $(`#${DOM_IDS.ID_FORMULARIO_OCULTO}`).attr('hidden', false);
}

function ocultarFormUno() {
    $(`#${DOM_IDS.ID_FORMULARIO_OCULTO}`).attr('hidden', true);
}

function guardarFormUno() {
    value = $(`#${DOM_IDS.INPUT_NAME}`)[0].value
    triggerSaveT1(value, triggerSaveT1Success, triggerSaveT1Error)
    ocultarFormUno()
}


function triggerSaveT1Success(data) {
    console.log(data)
    console.log('triggerSaveT1Success')
     $(`#${DOM_IDS.ID_REFERENCIA}`).append($('<option>', {
        value: data.id,
        text: data.name
    }));
    $(`#${DOM_IDS.ID_REFERENCIA} option[value=${data.id}]`).prop("selected", "selected")
}

function triggerSaveT1Error() {
    console.log('triggerSaveT1Error')
}

// SERVICE

function triggerSaveT1(value, successCallback, errorCallback) {

    params = {
        'name': value
    }
    $.ajax({
        contentType: 'application/json;charset=UTF-8',
        // headers: {
        // "Authorization": `Bearer ${token}`,
        // },
        data: JSON.stringify(params),
        error: errorCallback,
        success: successCallback,
        type: 'POST',
        url: `/api/create`,
    })
}