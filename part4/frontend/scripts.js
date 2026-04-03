document.addEventListener('DOMContentLoaded', () => {
    console.log("🚀 Script chargé !");
    checkAuthentication();
    
    // 💡 LOGIQUE DE ROUTAGE : On regarde sur quelle page on est
    if (document.getElementById('places-list')) {
        // On est sur index.html
        setupPriceFilter();
        fetchPlaces(); 
    } else if (document.getElementById('place-details')) {
        // On est sur place.html
        fetchPlaceDetails();
    }
});

// --- Cookies ---
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

// --- Auth ---
function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');
    if (loginLink) {
        loginLink.style.display = token ? 'none' : 'block';
    }
}

// --- TÂCHE 2 : FETCH LISTE (INDEX) ---
async function fetchPlaces() {
    const apiUrl = 'http://127.0.0.1:5000/api/v1/places/';
    try {
        const response = await fetch(apiUrl); // Plus besoin de token ici car c'est public
        if (response.ok) {
            const places = await response.json();
            displayPlaces(places);
        }
    } catch (error) {
        console.error('💥 Erreur réseau:', error);
    }
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    if (!placesList) return;

    placesList.innerHTML = ''; 
    places.forEach(place => {
        const card = document.createElement('div');
        card.className = 'place-card';
        const price = parseFloat(place.price) || 0;

        card.setAttribute('data-price', price);
        card.innerHTML = `
            <img src="images/place1.jpg" alt="${place.title}">
            <h3>${place.title}</h3>
            <p><strong>$${price}</strong> per night</p>
            <a href="place.html?id=${place.id}" class="details-button">View Details</a>
        `;
        placesList.appendChild(card);
    });
}

// --- TÂCHE 3 : FETCH DÉTAILS (PLACE.HTML) ---
async function fetchPlaceDetails() {
    const params = new URLSearchParams(window.location.search);
    const placeId = params.get('id');
    if (!placeId) return;

    try {
        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`);
        if (response.ok) {
            const place = await response.json();
            
            // Injection dynamique des données
            document.getElementById('place-title').textContent = place.title;
            document.getElementById('place-price').textContent = place.price;
            document.getElementById('place-description').textContent = place.description;
            document.getElementById('place-host').textContent = `${place.owner.first_name} ${place.owner.last_name}`;
            
            // Équipements
            const amenitiesContainer = document.getElementById('amenities-list');
            amenitiesContainer.innerHTML = '';
            place.amenities.forEach(amenity => {
                const span = document.createElement('span');
                span.className = 'amenity-tag';
                span.textContent = amenity.name;
                amenitiesContainer.appendChild(span);
            });

            // Reviews
            displayReviews(place.reviews);

            // Tâche 4 : Afficher le bouton Review seulement si connecté
            if (getCookie('token')) {
                document.getElementById('add-review-section').style.display = 'block';
            }
        }
    } catch (error) {
        console.error("Erreur détails:", error);
    }
}

function displayReviews(reviews) {
    const container = document.getElementById('reviews-container');
    if (!container) return;
    container.innerHTML = '';
    if (!reviews || reviews.length === 0) {
        container.innerHTML = '<p>No reviews yet.</p>';
        return;
    }
    reviews.forEach(r => {
        const div = document.createElement('div');
        div.className = 'review-card';
        div.innerHTML = `
            <h4>User ID: ${r.user_id || 'Anonymous'}</h4>
            <p class="rating">${'★'.repeat(r.rating)}${'☆'.repeat(5-r.rating)}</p>
            <p>${r.text}</p>
        `;
        container.appendChild(div);
    });
}

// --- Filter ---
function setupPriceFilter() {
    const priceFilter = document.getElementById('price-filter');
    if (!priceFilter) return;
    priceFilter.addEventListener('change', (e) => {
        const max = e.target.value;
        document.querySelectorAll('.place-card').forEach(card => {
            const p = parseFloat(card.dataset.price);
            card.style.display = (max === 'all' || p <= parseFloat(max)) ? 'block' : 'none';
        });
    });
}