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



