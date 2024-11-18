// Fonction pour récupérer un cookie par son nom
function getCookie(name) {
    const cookieArr = document.cookie.split(';');
    for (let cookie of cookieArr) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + '=')) {
            return cookie.split('=')[1];
        }
    }
    return null;
}

// Vérifie si l'utilisateur est authentifié
function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
        fetchPlaces(token);
    }
}

// Récupère les lieux à partir de l'API
async function fetchPlaces(token) {
    try {
        const response = await fetch('https://your-api-url/places', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            },
        });

        if (response.ok) {
            const places = await response.json();
            displayPlaces(places);
        } else {
            console.error('Erreur lors de la récupération des lieux:', response.statusText);
        }
    } catch (error) {
        console.error('Erreur de requête:', error);
    }
}

// Affiche dynamiquement les lieux dans la section #places-list
function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    placesList.innerHTML = ''; // Vide le contenu actuel

    places.forEach(place => {
        const placeCard = document.createElement('div');
        placeCard.className = 'place-card';
        placeCard.innerHTML = `
            <h2>${place.name}</h2>
            <p>${place.description}</p>
            <p>Localisation : ${place.location}</p>
            <p>Prix : ${place.price}€ par nuit</p>
        `;
        placesList.appendChild(placeCard);
    });
}

// Filtre les lieux en fonction du prix sélectionné
document.getElementById('price-filter').addEventListener('change', (event) => {
    const selectedPrice = event.target.value;
    const places = document.querySelectorAll('.place-card');

    places.forEach(place => {
        const price = parseInt(place.querySelector('p:nth-child(4)').textContent.match(/\d+/)[0]);

        if (selectedPrice === 'all' || price <= parseInt(selectedPrice)) {
            place.style.display = 'block';
        } else {
            place.style.display = 'none';
        }
    });
});

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    checkAuthentication();
});
