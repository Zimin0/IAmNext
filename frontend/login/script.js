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
    
    alert(`Login attempt with email: ${email}`);
}

document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.main-container');
    container.style.opacity = '0';
    container.style.transform = 'translateY(20px)';
    setTimeout(() => {
        container.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
        container.style.opacity = '1';
        container.style.transform = 'translateY(0)';
    }, 100);
});
