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

