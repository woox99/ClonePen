// Fetch Pinned Items AJAX
// CHANGE TO GET REQUEST
const getPinnedItemsByActiveUser = () => {
    const csrfToken = document.querySelector('[name=csrf-token]').content;

    fetch('/clonepen.com/api/get-pinned-items/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
        }
    })
    .then(response => response.json())
    .then(data => {
        items = data['pinned-items'];
        // console.log(items)
        pinnedItemsElement = document.querySelector('.pinned-items');

        // Clear existing html
        // pinnedItemsElement.innerHTML = '';

        for (const pen of items) {
            let pinnedItemElement = document.querySelector('.pinned-item')
            // const iframe = document.createElement('iframe');
            // iframe = pinnedItemElement.querySelector('iframe')
            // iframe.srcdoc = `<body>${pen.html}<style>${pen.css}</style><script>${pen.js}</script></body>`;
            // pinnedItemElement.appendChild(iframe);
            
            pinnedItemsElement.appendChild(pinnedItemElement);
            pinnedItemsElement.appendChild(pinnedItemElement);
            // let windowWidth = window.innerWidth;
            // let scale;

            // if(windowWidth > 768){
            //     scale = 0.5 - (212 / windowWidth);
            // }
            // else{
            //     scale = 1.0 - (136 / windowWidth) ;
            // }
            // iframe.style.zoom = scale;
        }
    })
}

// Toggle Pin Item AJAX
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

// Fetch unread message count
document.addEventListener('DOMContentLoaded', () => {
    fetch('/clonepen.com/api/messages/unread-count/')
        .then(response => response.json())
        .then(data => {
            if (data.unread_count > 0) {
                document.getElementById('unread-count').innerText = data.unread_count;
            }
        })
        .catch(error => {
            console.error('Error fetching unread count:', error);
        });
});