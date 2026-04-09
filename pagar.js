const boton = document.getElementById('btn-comprar');
const etiquetaTexto = document.getElementById('mensaje-total');

function cambiarTexto() {
    etiquetaTexto.innerText = "¡Gracias por su compra!";
    etiquetaTexto.style.color = "green"; 
}

boton.addEventListener('click', cambiarTexto);