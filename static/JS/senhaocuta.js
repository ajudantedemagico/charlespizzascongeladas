function togglePassword() {
            const passwordInput = document.getElementById('senha');
            const toggleButton = passwordInput.nextElementSibling;

            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                toggleButton.textContent = '🔓'; 
            } else {
                passwordInput.type = 'password';
                toggleButton.textContent = '🔒'; 
            }
        }