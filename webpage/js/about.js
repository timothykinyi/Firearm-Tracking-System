document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.nav-link.about').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default link behavior
        fetch('about.html') // Load the content of the "About" page
            .then(response => response.text())
            .then(data => {
                document.getElementById('contentPlaceholder').innerHTML = data; // Inject the content into the placeholder <div>
            })
            .catch(error => console.error('Error:', error));
    });
});
