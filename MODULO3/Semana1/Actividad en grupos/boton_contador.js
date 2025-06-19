let valorContador = 0;

let historial = [];

function aumentarcontador() {
    valorContador++;

    if (!valorContador) {
        alert("El contador no esta funcionando");
    }

    historial.push (valorContador);

    if (valorContador % 2 == 0) {
        console.log("numero par");}
    else{
        console.log("Numero impar");
    }

    document.getElementById("contador").textContent = valorContador;

    mostrarhistorial();
}

function mostrarhistorial () {
    console.log ("Historial de clics:");
    for (let i = 0; i < historial.length; i++) {
    console.log (`Clic ${i + 1}: ${historial[i]}`);
    }
}

