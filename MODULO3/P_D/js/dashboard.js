const API_URL = "http://localhost:3000";
const user = JSON.parse(localStorage.getItem("user"));
const content = document.getElementById("content");

if (!user) {
  window.location.href = "not-found.html";
}

// Función para renderizar eventos
async function renderDashboard() {
  const res = await fetch(`${API_URL}/events`);
  const events = await res.json();

  if (user.role === "admin") {
    renderAdmin(events);
  } else if (user.role === "visitor") {
    renderVisitor(events);
  }
}

// Vista para administradores
function renderAdmin(events) {
  const html = `
    <h2>Bienvenido administrador, ${user.username}</h2>
    <a href="dashboard/events/create.html">➕ Crear evento</a>
    <ul>
      ${events
        .map(
          (event) => `
        <li>
          <strong>${event.title}</strong> - ${event.date} - Cupos: ${event.capacity}
          <a href="dashboard/events/edit.html?id=${event.id}">✏️ Editar</a>
          <button onclick="deleteEvent(${event.id})">🗑️ Eliminar</button>
        </li>
      `
        )
        .join("")}
    </ul>
  `;
  content.innerHTML = html;
}

// Vista para visitantes
function renderVisitor(events) {
  const html = `
    <h2>Hola ${user.username}, estos son los eventos disponibles</h2>
    <ul>
      ${events
        .map(
          (event) => `
        <li>
          <strong>${event.title}</strong> - ${event.date} - Cupos: ${event.capacity}
          <button onclick="registerToEvent(${event.id})">📝 Registrarse</button>
        </li>
      `
        )
        .join("")}
    </ul>
  `;
  content.innerHTML = html;
}

// ==============================
// Función para eliminar evento (admin)
// ==============================
async function deleteEvent(id) {
  if (confirm("¿Seguro que quieres eliminar este evento?")) {
    await fetch(`${API_URL}/events/${id}`, {
      method: "DELETE"
    });
    renderDashboard();
  }
}

// ==============================
// Función para registrarse a evento (visitante)
// ==============================
async function registerToEvent(eventId) {
  // Verificar si ya está registrado
  const res = await fetch(`${API_URL}/registrations?userId=${user.id}&eventId=${eventId}`);
  const existing = await res.json();

  if (existing.length > 0) {
    alert("Ya estás registrado en este evento.");
    return;
  }

  // Obtener evento
  const eventRes = await fetch(`${API_URL}/events/${eventId}`);
  const event = await eventRes.json();

  // Contar registros actuales
  const regRes = await fetch(`${API_URL}/registrations?eventId=${eventId}`);
  const currentRegs = await regRes.json();

  if (currentRegs.length >= event.capacity) {
    alert("Este evento ya está lleno.");
    return;
  }

  // Registrar
  const registration = {
    userId: user.id,
    eventId: eventId
  };

  await fetch(`${API_URL}/registrations`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(registration)
  });

  alert("Registro exitoso.");
}

// Cargar el dashboard
renderDashboard();
