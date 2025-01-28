// Scale iframes and pen links based on window width
document.addEventListener('DOMContentLoaded', function() {
    const iframes = document.querySelectorAll('iframe');
    const penLinks = document.querySelectorAll('.pen-link');
    const pages = document.querySelector('.pages')
    const mainContent = document.querySelector('.main-content')

    function scaleIframes() {
        let windowWidth = window.innerWidth;
        let scale;
        
        // Large screens
        if(windowWidth > 768){
            scale = 0.5 - (212 / windowWidth);

            let iframeHeight = iframes[0].offsetHeight * scale;
            iframeHeight = Math.ceil(iframeHeight);
            pages.style.height = `${ iframeHeight * 2  + 250 }px`;
            mainContent.style.height = `${ iframeHeight * 2  + 700 }px`;
        }
        // Mobile screens
        else{
            scale = 1.0 - (136 / windowWidth) ;
            
            let iframeHeight = iframes[0].offsetHeight * scale;
            iframeHeight = Math.ceil(iframeHeight);
            pages.style.height = `${ iframeHeight * 4  + 400 }px`;
            mainContent.style.height = `${ iframeHeight * 4  + 900 }px`;
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


// Toggle follow/unfollow button
const toggleFollow = (button, profileId) => {
    const csrfToken = document.querySelector('[name=csrf-token]').content;
    
    // console.log(button)
    fetch(`/clonepen.com/api/toggle-follow/${profileId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
        }
    })
    .then(response => response.json())
    .then(data => {
        if(data.following){
            button.innerHTML = '<i class="bi bi-person-dash me-2"></i>Unfollow'
            button.classList.remove('follow-btn')
            button.classList.add('unfollow-btn')
        }
        else{
            button.innerHTML = '<i class="bi bi-person-add me-2"></i>Follow'
            button.classList.remove('unfollow-btn')
            button.classList.add('follow-btn')
        }
    })
}

