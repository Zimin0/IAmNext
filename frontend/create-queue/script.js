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

function createQueue(event) {
    event.preventDefault();
    const queueName = document.getElementById('queueName').value;
    const maxParticipants = document.getElementById('maxParticipants').value;
    const queueDescription = document.getElementById('queueDescription').value;
    const privateAccess = document.getElementById('privateAccess').checked;
    
    let message = `Queue "${queueName}" created. Maximum participants: ${maxParticipants}. ${privateAccess ? 'Access by link only.' : 'Public access.'}`;
    if (queueDescription) {
        message += `\nDescription: ${queueDescription}`;
    }
    
    alert(message);
}

document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.container');
    container.style.opacity = '0';
    container.style.transform = 'translateY(20px)';
    setTimeout(() => {
        container.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
        container.style.opacity = '1';
        container.style.transform = 'translateY(0)';
    }, 100);
});
