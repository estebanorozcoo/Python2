//Inicio del programa//
console.log("Bienvenido al sistema de mensajes");

//Solicitud de datos//
let nombre = prompt("Ingresa tu nombre: ");
let edad = prompt("Ingresa tu edad: ");

//Validacion de numero al ingrear edad//
edad = parseInt(edad);

//Validadcion de datos ingresados y salidad de mensaje correspondiente//
if(isNaN(edad)) {
    console.error("Error, por favor ingresa una edad valida en numeros");}
else if (edad <18) {
    alert(`Hola ${nombre}, eres menor de edad. ¡sigue aprendiendo y disfruta del codigo!`);}
else {
    alert(`Hola ${nombre}, eres mayor de edad. Prepárate para grandes oportunidades en el mundo de la programacion`);}
