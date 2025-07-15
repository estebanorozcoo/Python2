const API_URL = "http://localhost:3000";
const user = JSON.parse(localStorage.getItem("user"));
const params = new URLSearchParams(window.location.search);
const eventId = params.get("id");
const form = document.getElementById("eventForm");

// Proteger la vista para solo administradores
if (!user || user.role !== "admin") {
  window.location.href = "../../not-found.html";
}

// =====================
// Cargar datos si es edición
// =====================
if (eventId) {
  fetch(`${API_URL}/events/${eventId}`)
    .then((res) => res.json())
    .then((event) => {
      form.title.value = event.title;
      form.date.value = event.date;
      form.capacity.value = event.capacity;
    });
}

// =====================
// Crear o editar evento
// =====================
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const eventData = {
    title: form.title.value.trim(),
    date: form.date.value,
    capacity: parseInt(form.capacity.value)
  };

  if (!eventData.title || !eventData.date || isNaN(eventData.capacity)) {
    alert("Todos los campos son obligatorios.");
    return;
  }

  if (eventId) {
    // Actualizar evento
    await fetch(`${API_URL}/events/${eventId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(eventData)
    });
    alert("Evento actualizado.");
  } else {
    // Crear evento
    await fetch(`${API_URL}/events`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(eventData)
    });
    alert("Evento creado.");
  }

  window.location.href = "../../dashboard.html";
});
