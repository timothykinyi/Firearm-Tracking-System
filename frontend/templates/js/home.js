const imageUrls = [
    "images/altlogo.jpg",
    "images/bg.jpg",
    "images/holster1.jpg",
    // Add more image URLs as needed
];

let currentIndex = 0;
const intervalDuration = 3000; // Change image every 3 seconds

function setRandomBackground() {
    const dynamicBackground = document.getElementById('dynamic-background-container');

    // Load images into the container
    imageUrls.forEach((imageUrl) => {
        const img = document.createElement('img');
        img.src = imageUrl;
        dynamicBackground.appendChild(img);
    });

    // Start automatic image change timer
    setInterval(() => {
        currentIndex = (currentIndex + 1) % imageUrls.length;
        updateBackgroundPosition();
    }, intervalDuration);
}

function updateBackgroundPosition() {
    const dynamicBackground = document.getElementById('dynamic-background-container');
    const imgWidth = dynamicBackground.clientWidth;
    dynamicBackground.style.transform = `translateX(-${currentIndex * imgWidth}px)`;
}

window.onload = function() {
    setRandomBackground();
};
