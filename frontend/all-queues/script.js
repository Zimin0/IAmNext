const queueContainer = document.querySelector('.container');
const apiUrl = 'http://127.0.0.1:8000/queues/';

async function fetchQueues() {
    try {
        const response = await fetch(apiUrl);
        const queues = await response.json();

        renderQueues(queues);
    } catch (error) {
        console.error('Ошибка при получении очередей:', error);
    }
}

function renderQueues(queues) {
    const header = document.createElement('h1');
    header.textContent = 'Open queues';

    queueContainer.innerHTML = '';
    queueContainer.appendChild(header);

    queues.forEach(queue => {
        const link = document.createElement('a');
        link.href = `/one-queue/?id=${queue.id}`; // <-- ссылка на конкретную очередь
        link.className = 'queue';

        link.innerHTML = `
            <div class="queue-header">
                <div class="queue-name">${queue.title}</div>
                <div class="queue-count" id="queue-count-${queue.id}">
                    ${queue.member_count}/${queue.max_amount}
                </div>
            </div>
            <div class="queue-description">${queue.description}</div>
        `;

        queueContainer.appendChild(link);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    console.log("Подтягиваю очереди...");
    fetchQueues();
});
