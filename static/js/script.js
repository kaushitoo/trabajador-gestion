

let correo = "francisco@gmail.com";
let clave = "pass1234";

const btnForm = document.getElementById("btnFormulario");
const inputCorreo = document.getElementById("floatingInput");
const inputPass = document.getElementById("floatingPassword");
const img = document.getElementById("img");

const alerta = document.getElementById("alerta");

const validarFormulario = () =>{
    let valCorreo = false
    let valPass = false
    console.log(inputCorreo.value,inputPass.value)
    if ( inputPass.value.length == 0 || inputCorreo.value.length == 0){
        alerta .innerHTML =  '<div class="alert alert-danger" role="alert">El o los campos estan vacios!</div>'
        return false
    }
    if( inputCorreo.value == correo){
        valCorreo = true
    }else{
        alerta .innerHTML =  '<div class="alert alert-danger" role="alert">Correo invalido!</div>'
    }
    if( inputPass.value == clave){
        valPass = true
    }else{
        alerta .innerHTML =  '<div class="alert alert-danger" role="alert">Clave invalida</div>'
    }
    if (valCorreo && valPass){
        alerta .innerHTML =  '<div class="alert alert-primary" role="alert">Ingreso correctamente</div>'
        return true
    }
    return false
};




btnForm.addEventListener('click',()=>{
    if (validarFormulario()){
        window.location.assign("/inicio");
    }else{
        return
    }
});
