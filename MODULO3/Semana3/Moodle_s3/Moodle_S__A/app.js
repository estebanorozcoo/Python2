import { get } from "./scripts/crud";

const container = document.getElementById('content');

const routes = {
    "/": "./pages/home.html",
    "/dashboard": "./pages/dashboard.html"
}

function router() {
    const hash = window.location.hash.slice(1);
    const file = routes[hash];

    fetch(file)
    .then(res => res.text())
    .then(data => {
        container.innerHTML = data;

        if (hash === '/login') {
            
        }

    })
}

async function ejecutarGet() {
    const respuestaGet = await get('/users');

    console.log(respuestaGet)
}

ejecutarGet()

window.addEventListener("load", router);
window.addEventListener("hashchange", router);