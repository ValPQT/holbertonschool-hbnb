document.addEventListener('DOMContentLoaded', () => {
    console.log("🚀 Script chargé !");
    checkAuthentication();
    
    if (document.getElementById('places-list')) {
        setupPriceFilter();
        fetchPlaces(); 
    } else if (document.getElementById('place-details')) {
        fetchPlaceDetails();
    } else if (document.getElementById('review-form')) {
        setupReviewForm();
    } else if (document.getElementById('login-form')) {
        setupLoginForm();
    }
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');
    if (loginLink) {
        loginLink.style.display = token ? 'none' : 'block';
    }
}

async function setupLoginForm() {
    const loginForm = document.getElementById('login-form');
    if (!loginForm) return;

    loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        try {
            const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            if (response.ok) {
                const data = await response.json();
                document.cookie = `token=${data.access_token}; path=/; max-age=3600`;
                window.location.href = 'index.html';
            } else {
                alert("Erreur : Identifiants invalides.");
            }
        } catch (error) { console.error("Erreur API Login:", error); }
    });
}

// --- AFFICHAGE DE L'INDEX ---
async function fetchPlaces() {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/places/');
        if (response.ok) {
            const places = await response.json();
            displayPlaces(places);
        }
    } catch (error) { console.error('Erreur Places:', error); }
}

function displayPlaces(places) {
    const container = document.getElementById('places-list');
    if (!container) return;
    container.innerHTML = ''; 
    places.forEach((place, index) => {
        // Calcule le numéro de l'image (1, 2, 3 ou 4)
        const imgNum = (index % 4) + 1; 
        const card = document.createElement('div');
        card.className = 'place-card';
        card.setAttribute('data-price', place.price);
        card.innerHTML = `
            <img src="images/place${imgNum}.jpg" alt="${place.title}">
            <h3>${place.title}</h3>
            <p><strong>$${place.price}</strong> per night</p>
            <a href="place.html?id=${place.id}&img=${imgNum}" class="details-button">View Details</a>
        `;
        container.appendChild(card);
    });
}

// --- AFFICHAGE DES DÉTAILS (place.html) ---
async function fetchPlaceDetails() {
    const params = new URLSearchParams(window.location.search);
    const placeId = params.get('id');
    // MODIFICATION : On récupère le numéro de l'image depuis l'URL
    const imgNum = params.get('img') || '1'; 
    
    if (!placeId) return;

    try {
        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`);
        if (response.ok) {
            const place = await response.json();
            
            // Mise à jour des textes
            document.getElementById('place-title').textContent = place.title;
            document.getElementById('place-price').textContent = place.price;
            document.getElementById('place-host').textContent = `${place.owner.first_name} ${place.owner.last_name}`;
            
            const descElem = document.getElementById('place-description');
            if (descElem) descElem.textContent = place.description;

            // MODIFICATION : Mise à jour dynamique de l'image de couverture avec le bon numéro
            const detailImg = document.querySelector('#place-details img');
            if (detailImg) {
                detailImg.src = `images/place${imgNum}.jpg`; 
            }

            const addReviewBtn = document.querySelector('.add-review-btn');
            if (addReviewBtn) {
                // On transmet aussi le numéro d'image pour le formulaire de review
                addReviewBtn.href = `add_review.html?id=${place.id}&img=${imgNum}`;
            }

            displayReviews(place.reviews);

            if (getCookie('token')) {
                const section = document.getElementById('add-review-section');
                if (section) section.style.display = 'block';
            }
        }
    } catch (error) { console.error("Erreur Details:", error); }
}

function displayReviews(reviews) {
    const container = document.getElementById('reviews-container');
    if (!container) return;
    container.innerHTML = reviews && reviews.length > 0 ? '' : '<p>No reviews yet.</p>';
    reviews?.forEach(r => {
        const div = document.createElement('div');
        div.className = 'review-card';
        div.innerHTML = `
            <h4>User ID: ${r.user_id}</h4>
            <p class="rating">${'★'.repeat(r.rating)}${'☆'.repeat(5-r.rating)}</p>
            <p>${r.text}</p>
        `;
        container.appendChild(div);
    });
}

async function setupReviewForm() {
    const form = document.getElementById('review-form');
    const params = new URLSearchParams(window.location.search);
    const placeId = params.get('id');
    if (!form || !placeId) return;

    try {
        const res = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`);
        if (res.ok) {
            const place = await res.json();
            const titleElem = document.querySelector('.add-review p'); 
            if (titleElem) titleElem.innerHTML = `Reviewing: <strong>${place.title}</strong>`;
        }
    } catch (e) { console.error(e); }

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const token = getCookie('token');
        const text = document.getElementById('review').value;
        const rating = document.getElementById('rating').value;

        if (!token) { alert("You must be logged in!"); return; }

        try {
            const response = await fetch(`http://127.0.0.1:5000/api/v1/reviews/`, {
                method: 'POST',
                headers: { 
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}` 
                },
                body: JSON.stringify({ place_id: placeId, text: text, rating: parseInt(rating) })
            });

            if (response.ok) {
                alert("Review added!");
                // On récupère imgNum pour retourner à la page détails avec la bonne image
                const imgNum = params.get('img') || '1';
                window.location.href = `place.html?id=${placeId}&img=${imgNum}`;
            } else { alert("Error during submission."); }
        } catch (error) { console.error("Erreur POST review:", error); }
    });
}

function setupPriceFilter() {
    const filter = document.getElementById('price-filter');
    if (!filter) return;
    filter.addEventListener('change', (e) => {
        const max = e.target.value;
        document.querySelectorAll('.place-card').forEach(c => {
            const p = parseFloat(c.dataset.price);
            c.style.display = (max === 'all' || p <= parseFloat(max)) ? 'block' : 'none';
        });
    });
}