const queueDisplay = document.getElementById('queue-display');
const nicknameForm = document.getElementById('nickname-form');
const nicknameInput = document.getElementById('nickname-input');
const remainingPlacesDisplay = document.getElementById('remaining-places');
const showBlocksBtn = document.getElementById('showBlocksBtn');
let queue = ['Alice', 'Bob', 'Charlie'];
const maxQueueSize = 10;

function updateQueueDisplay() {
    queueDisplay.innerHTML = '';
    queue.forEach((nickname, index) => {
        const queueItem = document.createElement('div');
        queueItem.className = 'queue-item';
        queueItem.innerHTML = `
            <span>${index + 1}. ${nickname}</span>
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
    remainingPlacesDisplay.textContent = freePlaces;
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
    updateQueueDisplay();
});
