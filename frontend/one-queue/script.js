const queueDisplay = document.getElementById('queue-display');
const nicknameForm = document.getElementById('nickname-form');
const nicknameInput = document.getElementById('nickname-input');
const remainingPlacesDisplay = document.getElementById('remaining-places');
const showBlocksBtn = document.getElementById('showBlocksBtn');

let queue = [];
let maxQueueSize = 0;

function getQueueIdFromUrl() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

async function loadQueueData(queueId) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/queues/${queueId}/`);
        if (!response.ok) {
            throw new Error('Не удалось загрузить очередь');
        }
        const data = await response.json();

        // обновляем значения
        maxQueueSize = data.max_amount;
        queue = data.members;

        document.getElementById('queue-title').textContent = data.title;
        document.getElementById('queue-description').textContent = data.description;

        updateQueueDisplay();
    } catch (error) {
        console.error('Ошибка загрузки очереди:', error);
    }
}

function updateQueueDisplay() {
    queueDisplay.innerHTML = '';

    queue.forEach((member, index) => {
        const queueItem = document.createElement('div');
        queueItem.className = 'queue-item';
        queueItem.innerHTML = `
            <span>${index + 1}. Пользователь #${member}</span>
            <button onclick="leaveQueue(${index})">Leave</button>
        `;
        queueDisplay.appendChild(queueItem);
    });

    for (let i = queue.length; i < maxQueueSize; i++) {
        const freePlace = document.createElement('div');
        freePlace.className = 'free-place';
        freePlace.textContent = `${i + 1}. Free Place`;
        queueDisplay.appendChild(freePlace);
    }

    updateRemainingPlaces();
}

function updateRemainingPlaces() {
    const freePlaces = maxQueueSize - queue.length;
    remainingPlacesDisplay.textContent = `${freePlaces}`;
}

function joinQueue(nickname) {
    if (queue.length < maxQueueSize) {
        queue.push(nickname);
        updateQueueDisplay();
        return true;
    } else {
        alert("The queue is full. Please try again later.");
        return false;
    }
}

function leaveQueue(index) {
    queue.splice(index, 1);
    updateQueueDisplay();
}

nicknameForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const nickname = nicknameInput.value.trim();
    if (nickname && joinQueue(nickname)) {
        nicknameInput.value = '';
    }
});

function hideBlock(blockId) {
    const block = document.getElementById(blockId);
    block.style.opacity = '0';
    block.style.transform = 'translateY(-20px)';
    setTimeout(() => {
        block.style.display = 'none';
        updateShowBlocksButton();
    }, 300);
}

function toggleBlocks() {
    const blocks = ['description-block', 'remaining-places-block'];
    blocks.forEach(blockId => {
        const block = document.getElementById(blockId);
        if (block.style.display === 'none') {
            showBlock(blockId);
        }
    });
    updateShowBlocksButton();
}

document.addEventListener('DOMContentLoaded', () => {
    const queueId = getQueueIdFromUrl();
    if (queueId) {
        loadQueueData(queueId);
    } else {
        console.warn('Queue ID не указан в URL');
    }
});
