function showQueue() {
    alert("Displaying Queue");
}

function showAbout() {
    alert("Showing About Page");
}

function showContact() {
    alert("Showing Contact Page");
}

function login() {
    alert("Redirecting to Login Page");
}

function loginUser(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    // In a real application, there would be a server request here to authenticate the user
    
    alert(`Login attempt with email: ${email}`);
    // Redirect to user dashboard or display error message
}

// Add animation to container on page load
document.addEventListener('DOMContentLoaded', (event) => {
    const container = document.querySelector('.main-container');
    container.style.opacity = '0';
    container.style.transform = 'translateY(20px)';
    setTimeout(() => {
        container.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
        container.style.opacity = '1';
        container.style.transform = 'translateY(0)';
    }, 100);
});
