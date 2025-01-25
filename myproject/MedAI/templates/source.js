let slideIndex = 0;
showSlides();

function showSlides() {
    let slides = document.getElementsByClassName("mySlides");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    slides[slideIndex - 1].style.display = "block";  
    setTimeout(showSlides, 3000); // Change image every 3 seconds
}

function plusSlides(n) {
    showSlides(slideIndex += n);
}

document.getElementById('itinerary-form').addEventListener('submit', function(event) {
    event.preventDefault();
    document.getElementById('loading').style.display = 'block';
    setTimeout(function() {
        window.location.href = 'second-page.html'; // Redirect to second page after loading
    }, 3000); // Simulate loading time
});
