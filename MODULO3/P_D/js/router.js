// Obtener usuario logueado
function getUser() {
  return JSON.parse(localStorage.getItem("user"));
}

// Redirigir según condición
function redirectTo(path) {
  window.location.href = path;
}

// ==========================
// Validaciones de rutas
// ==========================

// Rutas protegidas para usuarios logueados
const protectedRoutes = [
  "/dashboard.html",
  "/dashboard/events/create.html",
  "/dashboard/events/edit.html"
];

// Rutas exclusivas para NO logueados
const authOnlyRoutes = ["/login.html", "/register.html"];

// Página actual
const currentPath = window.location.pathname;

// Usuario actual
const user = getUser();

// 1. Si la ruta es protegida y no hay sesión → redirigir a not-found
if (protectedRoutes.includes(currentPath) && !user) {
  redirectTo("not-found.html");
}

// 2. Si el usuario está logueado y entra a login o register → redirigir a dashboard
if (authOnlyRoutes.includes(currentPath) && user) {
  redirectTo("dashboard.html");
}

// 3. (Opcional) Si quieres mostrar el rol en consola para debug
if (user) {
  console.log(`Usuario logueado como ${user.username} (${user.role})`);
}
