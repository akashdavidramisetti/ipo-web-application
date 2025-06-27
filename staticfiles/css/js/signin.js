// Toggle password visibility
document.addEventListener('DOMContentLoaded', function () {
  const passwordInput = document.getElementById('password');
  const togglePassword = document.getElementById('togglePassword');

  if (togglePassword && passwordInput) {
    togglePassword.addEventListener('click', function () {
      const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
      passwordInput.setAttribute('type', type);
      this.classList.toggle('active');
    });
  }

  // Optional: console log checkbox toggle
  const keepSignedInCheckbox = document.getElementById('keep-signed-in');
  if (keepSignedInCheckbox) {
    keepSignedInCheckbox.addEventListener('change', function () {
      console.log('Keep me signed in:', this.checked);
    });
  }
});
