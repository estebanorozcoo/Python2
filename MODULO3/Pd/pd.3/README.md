# SPA Gestión de Eventos 🎉

Proyecto desarrollado como prueba de desempeño para el Módulo 3 de JavaScript.

---

## 📋 Descripción

Esta es una **Single Page Application (SPA)** para gestionar eventos, con sistema de autenticación por roles (admin y visitante), rutas protegidas, persistencia de sesión y operaciones CRUD conectadas a una base de datos simulada con `json-server`.

---

## 🧑‍💻 Datos del coder

- **Nombre:** Juan David Sierra
- **Clan:** Digit Deck
- **Correo:** juandavid@digitdeck.co
- **Documento:** 1111111111

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/spa-eventos.git
cd spa-eventos
```

### 2. Instalar dependencias

```bash
npm install
```

### 3. Ejecutar el servidor de base de datos (json-server)

```bash
npm run json-server
```

Esto levantará `json-server` en `http://localhost:3000` usando el archivo `db.json`.

### 4. Ejecutar la SPA

Puedes usar Live Server o correr con Vite (si configuraste uno):

```bash
npm run dev
```

---

## 🧪 Rutas de la SPA

| Vista                | Ruta                              | Acceso     |
|---------------------|-----------------------------------|------------|
| Home                | `/index.html`                     | Público    |
| Registro            | `/register.html`                  | Visitante  |
| Login               | `/login.html`                     | Público    |
| Dashboard           | `/dashboard.html`                 | Protegido  |
| Crear evento        | `/dashboard/events/create.html`   | Admin      |
| Editar evento       | `/dashboard/events/edit.html?id=ID` | Admin    |
| Página no autorizada| `/not-found.html`                 | Automática |

---

## 👥 Tipos de usuario

### Admin
- Puede crear, editar y eliminar eventos.
- Usuario creado por defecto en `db.json`:
  - **usuario:** admin
  - **contraseña:** admin123

### Visitante
- Puede registrarse e iniciar sesión.
- Puede inscribirse a eventos si hay cupo disponible.

---

## 🧰 Herramientas utilizadas

- HTML5 + CSS3
- JavaScript Vanilla (ES6+)
- json-server
- Local Storage
- Git

---

## 📬 Contacto

¿Dudas o mejoras? Puedes escribirme a **juandavid@digitdeck.co**. 🚀
