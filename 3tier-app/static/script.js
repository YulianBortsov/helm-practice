console.log('Static content served successfully!');

const backendServiceHost = "127.0.0.1";
const backendPort = "37093";

document.getElementById('createItemForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;

    try {
        const response = await fetch('http://${backendServiceHost}:${backendPort}/api/items', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, description }),
        });

        const data = await response.json();
        alert(data.message || 'Error occurred!');
    } catch (error) {
        console.error('Error during fetch:', error);
        alert('Error occurred!');
    }
});

async function loadItems() {
    try {
        const response = await fetch('http://${backendServiceHost}:${backendPort}/api/items');
        const items = await response.json();

        const itemsList = document.getElementById('itemsList');
        itemsList.innerHTML = '';
        items.forEach(item => {
            const listItem = document.createElement('li');
            listItem.textContent = `${item.name}: ${item.description || 'No description'}`;
            itemsList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error loading items:', error);
        alert('Error occurred while loading items!');
    }
}

