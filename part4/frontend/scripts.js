document.addEventListener('DOMContentLoaded', () => {


    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            // Empêche le rechargement de la page

            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            // Récupère les valeurs saisies par l'utilisateur

            await loginUser(email, password);
        });
    }
});

async function loginUser(email, password) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
            // Convertit l'objet JS en JSON pour l'envoyer à l'API
        });

        if (response.ok) {
            const data = await response.json();
            // Récupère la réponse JSON de l'API

            document.cookie = `token=${data.access_token}; path=/`;
            // Stocke le token JWT dans un cookie accessible sur toutes les pages (path=/)

            window.location.href = 'index.html';
            // Redirige vers la page principale

        } else {
            alert('Login failed: ' + response.statusText);
            // Affiche une erreur si le login échoue
        }

    } catch (error) {
        alert('An error occurred: ' + error.message);
        // Affiche une erreur si la requête échoue complètement (ex: API hors ligne)
    }
}