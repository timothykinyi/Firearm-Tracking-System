// Function to navigate to the specified page
function navigateTo(page) {
    // Logic to navigate to the specified page
    console.log("Navigating to", page);
}

// Add event listeners for hover effect
document.querySelectorAll('.nav-link').forEach(item => {
    item.addEventListener('mouseenter', event => {
        event.target.classList.add('text-primary', 'font-weight-bold');
    });
    item.addEventListener('mouseleave', event => {
        event.target.classList.remove('text-primary', 'font-weight-bold');
    });
    item.addEventListener('click', event => {
        // Prevent default link behavior
        event.preventDefault();
        // Get the page from the link's text content
        const page = event.target.textContent.trim();
        // Call the navigateTo function with the page
        navigateTo(page);
    });
});
