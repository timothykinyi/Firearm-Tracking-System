// Define an array of image URLs
const imageUrls = [
    'images/altlogo.jpg',
    'images/logo.jpg',
    
    // Add more image URLs as needed
];

// Function to set a random background image
function setRandomBackground() {
    const randomIndex = Math.floor(Math.random() * imageUrls.length);
    const imageUrl = imageUrls[randomIndex];
    document.getElementById('dynamic-background').style.backgroundImage = `url(${imageUrl})`;
}

// Call the function to set a random background image when the page loads
window.onload = function() {
    setRandomBackground();
};
