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
