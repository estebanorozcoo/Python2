// Paso 1: Creación del objeto productos
const productos = {
  producto1: { id: 1, nombre: "Teclado Mecánico", precio: 150000 },
  producto2: { id: 2, nombre: "Mouse Inalámbrico", precio: 85000 },
  producto3: { id: 3, nombre: "Monitor 24 pulgadas", precio: 650000 }
};

// Paso 2: Conversión a Set
const setProductos = new Set();
for (let key in productos) {
  const producto = productos[key];
  if (![...setProductos].some(p => p.id === producto.id)) {
    setProductos.add(producto);
  }
}

// Paso 3: Creación del Map
const mapCategorias = new Map();
mapCategorias.set("Periféricos", "Teclado Mecánico");
mapCategorias.set("Accesorios", "Mouse Inalámbrico");
mapCategorias.set("Pantallas", "Monitor 24 pulgadas");

// Paso 4: Mostrar datos en HTML
const listaObjeto = document.getElementById("listaObjeto");
const listaSet = document.getElementById("listaSet");
const listaMap = document.getElementById("listaMap");
const mensajeValidacion = document.getElementById("mensajeValidacion");

// Mostrar productos del objeto
for (let key in productos) {
  const p = productos[key];
  const item = document.createElement("li");
  item.textContent = `ID: ${p.id}, Nombre: ${p.nombre}, Precio: $${p.precio}`;
  listaObjeto.appendChild(item);
}

// Mostrar productos únicos del Set
for (let p of setProductos) {
  const item = document.createElement("li");
  item.textContent = `ID: ${p.id}, Nombre: ${p.nombre}, Precio: $${p.precio}`;
  listaSet.appendChild(item);
}

// Mostrar categorías del Map
mapCategorias.forEach((nombre, categoria) => {
  const item = document.createElement("li");
  item.textContent = `Categoría: ${categoria} → Producto: ${nombre}`;
  listaMap.appendChild(item);
});

// Validación
let datosCompletos = true;
setProductos.forEach(p => {
  if (!p.id || !p.nombre || !p.precio) {
    datosCompletos = false;
  }
});

mensajeValidacion.textContent = datosCompletos
  ? "Todos los productos tienen información completa"
  : "Hay productos con datos incompletos";
if (!datosCompletos) {
  mensajeValidacion.classList.add("error");
}
