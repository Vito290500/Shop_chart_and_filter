// Get the element by its id
const messageElement = document.getElementById('message');

// Function to hide the element after 3 seconds
function hideMessage() {
    messageElement.style.display = 'none';
}

// Check if the message element exists before attempting to hide it
if (messageElement) {
    // Call the hideMessage function after a 3-second delay (3000 milliseconds)
    setTimeout(hideMessage, 3000);
}