const imageUrls = [
    "images/altlogo.jpg",
    "images/bg.jpg",
    "images/holster1.jpg",
    // Add more image URLs as needed
];

let currentIndex = 0;
const intervalDuration = 3000; // Change image every 3 seconds

function setRandomBackground() {
    const container = document.getElementById('background-container');
    const dynamicBackground = document.getElementById('dynamic-background');
    const prevButton = document.getElementById('prev-button');
    const nextButton = document.getElementById('next-button');
    
    // Load images into the container
    imageUrls.forEach((imageUrl) => {
        const img = document.createElement('img');
        img.src = imageUrl;
        dynamicBackground.appendChild(img);
    });

    const imgWidth = container.clientWidth;
    dynamicBackground.style.width = `${imgWidth}px`; // Set width to fit one image

    // Set event listeners for the navigation buttons
    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + imageUrls.length) % imageUrls.length;
        updateBackgroundPosition();
    });

    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % imageUrls.length;
        updateBackgroundPosition();
    });

    // Start automatic image change timer
    setInterval(() => {
        currentIndex = (currentIndex + 1) % imageUrls.length;
        updateBackgroundPosition();
    }, intervalDuration);
}

function updateBackgroundPosition() {
    const container = document.getElementById('background-container');
    const dynamicBackground = document.getElementById('dynamic-background');
    const imgWidth = container.clientWidth;
    dynamicBackground.style.transform = `translateX(-${currentIndex * imgWidth}px)`;
}

window.onload = function() {
    setRandomBackground();
};
