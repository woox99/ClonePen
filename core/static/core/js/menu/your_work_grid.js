// Scale iframes and pen links based on window width
document.addEventListener('DOMContentLoaded', function() {
    const iframes = document.querySelectorAll('iframe');
    const penLinks = document.querySelectorAll('.pen-link');
    const pages = document.querySelector('.pages')
    const mainContent = document.querySelector('.main-content')

    function scaleIframes() {
        let windowWidth = window.innerWidth;
        let scale;
        
        if(windowWidth > 768){
            scale = 0.5 - (212 / windowWidth);

            let iframeHeight = iframes[0].offsetHeight * scale;
            iframeHeight = Math.ceil(iframeHeight);
            pages.style.height = `${ iframeHeight * 2  + 250 }px`;
            mainContent.style.height = `${ iframeHeight * 2  + 400 }px`;
        }
        else{
            scale = 1.0 - (136 / windowWidth) ;
            
            let iframeHeight = iframes[0].offsetHeight * scale;
            iframeHeight = Math.ceil(iframeHeight);
            pages.style.height = `${ iframeHeight * 4  + 400 }px`;
            mainContent.style.height = `${ iframeHeight * 4  + 550 }px`;
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



