// URL base del servidor json-server
const API_URL = "http://localhost:3000";

// ==========================
// REGISTRO DE USUARIO
// ==========================
async function registerUser(e) {
  e.preventDefault();

  const username = document.getElementById("regUsername").value.trim();
  const password = document.getElementById("regPassword").value.trim();
  const role = document.getElementById("role").value;

  if (!username || !password) {
    alert("Todos los campos son obligatorios.");
    return;
  }

  const res = await fetch(`${API_URL}/users?username=${username}`);
  const existing = await res.json();

  if (existing.length > 0) {
    alert("Este usuario ya existe.");
    return;
  }

  const newUser = {
    username,
    password,
    role
  };

  await fetch(`${API_URL}/users`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(newUser)
  });

  alert("Registro exitoso. Ahora puedes iniciar sesión.");
  window.location.href = "login.html";
}

// ==========================
// INICIO DE SESIÓN
// ==========================
async function loginUser(e) {
  e.preventDefault();

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();

  const res = await fetch(`${API_URL}/users?username=${username}&password=${password}`);
  const data = await res.json();

  if (data.length === 0) {
    alert("Usuario o contraseña incorrectos.");
    return;
  }

  const user = data[0];

  // Guardar sesión
  localStorage.setItem("user", JSON.stringify(user));

  // Redirigir al dashboard
  window.location.href = "dashboard.html";
}

// ==========================
// VERIFICAR SESIÓN ACTIVA
// ==========================
function checkSession() {
  const user = JSON.parse(localStorage.getItem("user"));
  return user;
}

// ==========================
// CERRAR SESIÓN
// ==========================
function logoutUser() {
  localStorage.removeItem("user");
  window.location.href = "login.html";
}

// ==========================
// EVENTOS
// ==========================

// Registro
const registerForm = document.getElementById("registerForm");
if (registerForm) registerForm.addEventListener("submit", registerUser);

// Login
const loginForm = document.getElementById("loginForm");
if (loginForm) loginForm.addEventListener("submit", loginUser);

// Logout
const logoutBtn = document.getElementById("logout");
if (logoutBtn) logoutBtn.addEventListener("click", logoutUser);
