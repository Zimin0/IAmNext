function showQueue() {
    alert("Showing Queue");
  }
  
  function showAbout() {
    alert("Showing About Page");
  }
  
  function showContact() {
    alert("Showing Contact Page");
  }
  
  function login() {
    alert("Opening Login Form");
  }
  
  function goHome() {
    window.location.href = "https://queue.com/";
  }
  
  // Add animation to elements on page load
  document.addEventListener('DOMContentLoaded', (event) => {
    const elements = document.querySelectorAll('h1, p, .progress-bar, button');
    elements.forEach((element, index) => {
      element.style.animation = `fadeIn 0.5s ease-out ${index * 0.1}s both`;
    });
  });
  