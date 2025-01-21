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
        console.log(items)
        pinnedItemsElement = document.querySelector('.pinned-items');

        // Clear existing html
        pinnedItemsElement.innerHTML = '';

        for (const pen of items) {
            // Create the row div
            const row = document.createElement('div');
            row.className = 'row';

            // Column 1: Title with link
            const col1 = document.createElement('div');
            col1.className = 'col-10 col-lg-5 cell';

            const titleLink = document.createElement('a');
            titleLink.href = `/clonepen.com/pen/${pen.slug}`
            titleLink.className = 'title';
            titleLink.innerText = pen.title;

            col1.appendChild(titleLink);

            const dateConfigure = { 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric', 
                hour: '2-digit', 
                minute: '2-digit' 
            };

            // Column 2: Created Date 
            const col2 = document.createElement('div');
            col2.className = 'col-3 cell d-none d-lg-flex';

            const createdDate = document.createElement('p');
            createdDate.className = 'table-data text-secondary';
            const created = new Date(pen.created);
            createdDate.innerText = created.toLocaleDateString('en-US', dateConfigure);

            col2.appendChild(createdDate);

            // Column 3: Modified Date 
            const col3 = document.createElement('div');
            col3.className = 'col-3 cell d-none d-lg-flex';

            const modifiedDate = document.createElement('p');
            modifiedDate.className = 'table-data text-secondary';
            const modified = new Date(pen.modified);
            modifiedDate.innerText = modified.toLocaleDateString('en-US', dateConfigure);

            col3.appendChild(modifiedDate);

            // Column 4: Pin Toggle Button
            const col4 = document.createElement('div');
            col4.className = 'col cell d-flex justify-content-center';

            const pinButton = document.createElement('button');
            pinButton.className = 'btn px-2 py-1';
            pinButton.setAttribute('onclick', `togglePin(this, ${pen.id})`);

            const pinIcon = document.createElement('i');
            pinIcon.className = 'bi bi-pin-fill fs-5';

            pinButton.appendChild(pinIcon);
            col4.appendChild(pinButton);

            // Append all columns to the row
            row.appendChild(col1);
            row.appendChild(col2);
            row.appendChild(col3);
            row.appendChild(col4);

            // Append the row to the pinned-items container
            pinnedItemsElement.appendChild(row);
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
        });
})