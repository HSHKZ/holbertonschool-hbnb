document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const errorMessage = document.getElementById('error-message');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // Empêche le comportement par défaut du formulaire
            
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('https://your-api-url/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ email, password }),
                });

                if (response.ok) {
                    const data = await response.json();
                    // Stocker le token dans un cookie
                    document.cookie = `token=${data.access_token}; path=/`;
                    // Redirection vers la page principale
                    window.location.href = 'index.html';
                } else {
                    // Afficher un message d'erreur en cas d'échec
                    errorMessage.textContent = 'Échec de la connexion. Vérifiez vos identifiants.';
                    errorMessage.style.display = 'block';
                }
            } catch (error) {
                console.error('Erreur:', error);
                errorMessage.textContent = 'Une erreur est survenue. Veuillez réessayer.';
                errorMessage.style.display = 'block';
            }
        });
    }
});

