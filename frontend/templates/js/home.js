$(document).ready(function() {
    // Array of image URLs
    var images = ['', 'image2.jpg', 'image3.jpg'];
    var currentIndex = 0;

    // Function to change background image
    function changeBackground() {
        $('#dynamic-background-container').css('background-image', 'url(images/' + images[currentIndex] + ')');
        currentIndex = (currentIndex + 1) % images.length;
    }

    // Call changeBackground function initially
    changeBackground();

    // Set interval to change background image every 5 seconds
    setInterval(changeBackground, 5000);

    // Array of words to animate
    var words = ['Gun', 'Holder', 'Tracking', 'Management', 'System'];
    var wordIndex = 0;

    // Function to animate words
    function animateWords() {
        $('#animating-word').text(words[wordIndex]);
        wordIndex = (wordIndex + 1) % words.length;
    }

    // Call animateWords function initially
    animateWords();

    // Set interval to animate words every 2 seconds
    setInterval(animateWords, 2000);
});
