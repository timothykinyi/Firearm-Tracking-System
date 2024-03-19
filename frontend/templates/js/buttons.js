// Scroll to the "About Us" section when the button is clicked
document.getElementById('about-us-btn').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default link behavior
    document.getElementById('about-us').scrollIntoView({ behavior: 'smooth' }); // Scroll to the element with ID "about-us" smoothly
});
