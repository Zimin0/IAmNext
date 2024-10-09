function showQueue() {
    alert("Showing Queue");
}

function showAbout() {
    alert("Showing About Page");
}

function showContact() {
    alert("You are already on the Contact Page");
}

function login() {
    alert("Opening Login Form");
}

// Add animation to containers on page load
document.addEventListener('DOMContentLoaded', (event) => {
    const containers = document.querySelectorAll('.container, .ticket-container');
    containers.forEach(container => {
        container.style.opacity = '0';
        container.style.transform = 'translateY(20px)';
        setTimeout(() => {
            container.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
            container.style.opacity = '1';
            container.style.transform = 'translateY(0)';
        }, 100);
    });
});

// Form submission handling
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Simulate ticket creation
    const ticketId = Math.floor(Math.random() * 1000000);
    
    // Create new ticket element
    const ticketElement = document.createElement('div');
    ticketElement.className = 'ticket-status';
    ticketElement.innerHTML = `
        <h3>Ticket #${ticketId}</h3>
        <p><span class="status-indicator status-new"></span> <span class="status-text">New</span></p>
    `;
    
    // Add new ticket to the list
    const ticketList = document.getElementById('ticketList');
    ticketList.insertBefore(ticketElement, ticketList.firstChild);
    
    // Simulate status changes
    setTimeout(() => {
        ticketElement.querySelector('.status-indicator').className = 'status-indicator status-in-progress';
        ticketElement.querySelector('.status-text').textContent = 'In Progress';
    }, 3000);
    
    setTimeout(() => {
        ticketElement.querySelector('.status-indicator').className = 'status-indicator status-resolved';
        ticketElement.querySelector('.status-text').textContent = 'Resolved';
    }, 6000);

    this.reset();
});
