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