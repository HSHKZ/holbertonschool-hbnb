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

