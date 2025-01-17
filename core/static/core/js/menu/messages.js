// Set max-height of list-group element
document.addEventListener('DOMContentLoaded', function() {
    const listGroup = document.querySelector('.list-group')
    const sideBar = document.querySelector('.sidebar')
    const mainContent = document.querySelector('.main-content')
    
    function setMaxHeight() {
        let windowWidth = window.innerWidth;
        let sideBarHeight = sideBar.offsetHeight;
        if(windowWidth > 768){
            // listGroup.style.height = (`${sideBarHeight - 70}px`);
            mainContent.style.height = (`${sideBarHeight - 70}px`);
        }
        else{
            mainContent.style.height = 'calc(100vh - 70px)';
        }
    }

    // Set initial max-height on load
    setMaxHeight();

    // Adjust scale on window resize
    window.addEventListener('resize', setMaxHeight);
});

// Set chat-box scrolled to end of conversation
document.addEventListener('DOMContentLoaded', () => {
    const chatElement = document.querySelector('.chat');
    chatElement.scrollTop = chatElement.scrollHeight;
});