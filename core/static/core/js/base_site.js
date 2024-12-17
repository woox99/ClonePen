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