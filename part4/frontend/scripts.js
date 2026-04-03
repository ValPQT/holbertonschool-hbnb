document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialisation de l'affichage (Auth + Fetch)
    checkAuthentication();

    // 2. Initialisation de l'écouteur pour le filtrage par prix
    setupPriceFilter();
});

// --- Gestion des Cookies ---
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

// --- Vérification de l'Authentification ---
function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.querySelector('.login-button'); // Cible ton bouton Login

    if (!token) {
        if (loginLink) loginLink.style.display = 'block';
        // Optionnel : charger les places même sans token si l'API est publique
        fetchPlaces(null);
    } else {
        if (loginLink) loginLink.style.display = 'none';
        fetchPlaces(token);
    }
}

// --- Récupération des données API ---
async function fetchPlaces(token) {
    const apiUrl = 'http://127.0.0.1:5000/api/v1/places/'; // URL à vérifier selon ton backend
    const headers = { 'Content-Type': 'application/json' };
    
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }

    try {
        const response = await fetch(apiUrl, { method: 'GET', headers: headers });
        if (response.ok) {
            const places = await response.json();
            displayPlaces(places);
        } else {
            console.error('Erreur lors de la récupération des lieux');
        }
    } catch (error) {
        console.error('Erreur réseau :', error);
    }
}

// --- Affichage Dynamique des Lieux ---
function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    if (!placesList) return;

    // Vide les cartes statiques actuelles du HTML
    placesList.innerHTML = '';

    places.forEach(place => {
        // Création de l'élément article/div
        const card = document.createElement('div');
        card.classList.add('place-card');
        
        // On stocke le prix dans un attribut data- pour le filtre JS
        const price = place.price_by_night || place.price || 0;
        card.setAttribute('data-price', price);

        // Injection du HTML (Structure identique à ton CSS)
        card.innerHTML = `
            <img src="${place.image_url || 'images/place1.jpg'}" alt="${place.name}">
            <h3>${place.name || place.title}</h3>
            <p>$${price} per night</p>
            <a href="place.html?id=${place.id}" class="details-button">View Details</a>
        `;

        placesList.appendChild(card);
    });
}

// --- Filtrage Client-Side ---
function setupPriceFilter() {
    const priceFilter = document.getElementById('price-filter');
    if (!priceFilter) return;

    priceFilter.addEventListener('change', (event) => {
        const selectedMaxPrice = event.target.value;
        const allCards = document.querySelectorAll('.place-card');

        allCards.forEach(card => {
            const cardPrice = parseFloat(card.getAttribute('data-price'));

            if (selectedMaxPrice === 'all') {
                card.style.display = 'block';
            } else {
                const max = parseFloat(selectedMaxPrice);
                // On affiche uniquement si le prix est inférieur ou égal au filtre
                card.style.display = (cardPrice <= max) ? 'block' : 'none';
            }
        });
    });
}