document.addEventListener('DOMContentLoaded', () => {
  const chatForm = document.getElementById('chat-form');
  const userInput = document.getElementById('user-input');
  const chatMessages = document.getElementById('chat-messages');

  chatForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const message = userInput.value.trim();
      if (!message) return;

      // Add user message to chat
      addMessageToChat('You', message);

      // Clear input
      userInput.value = '';

      try {
          // Send message to server
          const response = await fetch('/api/chat', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ message: message }),
          });

          if (!response.ok) {
              throw new Error('Network response was not ok');
          }

          const data = await response.json();
          
          // Add bot response to chat
          addMessageToChat('Bot', data.response);
      } catch (error) {
          console.error('Error:', error);
          addMessageToChat('Error', 'Failed to get response from the server.');
      }
  });

  function addMessageToChat(sender, message) {
      const messageElement = document.createElement('div');
      messageElement.className = `${sender.toLowerCase()}-message`;  // Corrected string interpolation
      messageElement.textContent = `${sender}: ${message}`;  // Corrected string interpolation
      chatMessages.appendChild(messageElement);
      chatMessages.scrollTop = chatMessages.scrollHeight;
  }
});