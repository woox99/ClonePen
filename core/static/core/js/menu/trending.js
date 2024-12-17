// Scale iframes and pen links based on window width
document.addEventListener('DOMContentLoaded', function() {
    const iframes = document.querySelectorAll('iframe');
    const penLinks = document.querySelectorAll('.pen-link');
    
    function scaleIframes() {
        let windowWidth = window.innerWidth;
        let scale;
        if(windowWidth > 768){
            scale = 0.5 - (212 / windowWidth);
        }
        else{
            scale = 1.0 - (136 / windowWidth) ;
        }
        
        for (const iframe of iframes) {
            iframe.style.zoom = scale;
        }
        for ( const penLink of penLinks) {
            penLink.style.zoom = scale;
        }
    }

    // Set initial scale on load
    scaleIframes();

    // Adjust scale on window resize
    window.addEventListener('resize', scaleIframes);
});


// Pinned Item AJAX
const togglePin = (button, penId) => {
    const csrfToken = document.querySelector('[name=csrf-token]').content;
    const icon = button.querySelector('i')

    fetch(`/clonepen.com/api/toggle-pin/${penId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.pinned) {
            icon.classList.remove('bi-pin');
            icon.classList.add('bi-pin-fill');
        }
        else {
            icon.classList.remove('bi-pin-fill');
            icon.classList.add('bi-pin')
        }
    })

    
}
