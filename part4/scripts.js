// Récupère l'ID du lieu à partir de l'URL
function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('placeId');
}

// Récupère un cookie par son nom
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
    const addReviewSection = document.getElementById('add-review');

    if (!token) {
        addReviewSection.style.display = 'none';
    } else {
        addReviewSection.style.display = 'block';
        fetchPlaceDetails(token, getPlaceIdFromURL());
    }
}

// Récupère les détails du lieu à partir de l'API
async function fetchPlaceDetails(token, placeId) {
    try {
        const response = await fetch(`https://your-api-url/places/${placeId}`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            },
        });

        if (response.ok) {
            const place = await response.json();
            displayPlaceDetails(place);
        } else {
            console.error('Erreur lors de la récupération des détails du lieu:', response.statusText);
        }
    } catch (error) {
        console.error('Erreur de requête:', error);
    }
}

// Affiche dynamiquement les détails du lieu
function displayPlaceDetails(place) {
    const placeDetails = document.getElementById('place-details');
    placeDetails.innerHTML = `
        <h1>${place.name}</h1>
        <p>${place.description}</p>
        <p>Prix : ${place.price}€ par nuit</p>
        <h3>Commodités :</h3>
        <ul>
            ${place.amenities.map(amenity => `<li>${amenity}</li>`).join('')}
        </ul>
        <h3>Avis :</h3>
        <div id="reviews">
            ${place.reviews.length > 0 ? place.reviews.map(review => `<p>${review}</p>`).join('') : '<p>Aucun avis pour le moment.</p>'}
        </div>
    `;
}

// Soumet un nouvel avis
async function submitReview(event) {
    event.preventDefault();

    const token = getCookie('token');
    const placeId = getPlaceIdFromURL();
    const reviewText = document.getElementById('review-text').value;

    try {
        const response = await fetch(`https://your-api-url/places/${placeId}/reviews`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ review: reviewText }),
        });

        if (response.ok) {
            const updatedPlace = await response.json();
            displayPlaceDetails(updatedPlace);
            document.getElementById('review-form').reset();
        } else {
            console.error('Erreur lors de l\'ajout de l\'avis:', response.statusText);
        }
    } catch (error) {
        console.error('Erreur de requête:', error);
    }
}

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    checkAuthentication();
    document.getElementById('review-form').addEventListener('submit', submitReview);
});
