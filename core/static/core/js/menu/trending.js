document.addEventListener('DOMContentLoaded', function() {
    const iframes = document.querySelectorAll('iframe');

    
    // Scale iframes based on window width
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
            // iframe.style.transform = `scale(${scale})`;
            iframe.style.zoom = scale;
        }
    }

    // Set initial scale on load
    scaleIframes();

    // Adjust scale on window resize
    window.addEventListener('resize', scaleIframes);
});
