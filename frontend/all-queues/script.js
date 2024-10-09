function updateQueueCount(queueId, max) {
    const countElement = document.getElementById(queueId);
    const currentCount = parseInt(countElement.textContent.split('/')[0]);
    let newCount = currentCount + Math.floor(Math.random() * 3) - 1; // -1, 0, or 1
    newCount = Math.max(0, Math.min(newCount, max)); // Ensure count is between 0 and max
    countElement.textContent = `${newCount}/${max}`;
  }
  
  // Update queue counts every 3 seconds
  setInterval(() => {
    updateQueueCount('express-count-1', 10);
    updateQueueCount('express-count-2', 10);
    updateQueueCount('regular-count', 10);
    updateQueueCount('vip-count', 10);
  }, 3000);
  
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
  
  // Add animation to queue elements on page load
  document.addEventListener('DOMContentLoaded', (event) => {
      const queues = document.querySelectorAll('.queue');
      queues.forEach((queue, index) => {
          queue.style.animation = `fadeIn 0.5s ease-out ${index * 0.1}s both`;
      });
  });
  