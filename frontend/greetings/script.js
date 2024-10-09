import { getToken } from '../api_scripts/queue.js';

getToken();


function showQueue() {
    alert("Showing Queue");
}

function showAbout() {
    alert("Showing About Page");
}

function showContact() {
    alert("Showing Contact Page");
}

function login() {
    alert("Opening Login Form");
}

function createQueue() {
    alert("Creating a new queue");
}

function joinQueue() {
    alert("Joining existing queue");
}

document.addEventListener('DOMContentLoaded', (event) => {
    const container = document.querySelector('.container');
    container.style.opacity = '0';
    container.style.transform = 'translate(-50%, -48%)';
    setTimeout(() => {
        container.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
        container.style.opacity = '1';
        container.style.transform = 'translate(-50%, -50%)';
    }, 100);

    const backgroundAnimation = document.querySelector('.background-animation');
    const blueShades = ['#4D94FF', '#66A3FF', '#80B3FF', '#99C2FF', '#B3D1FF'];
    const numberOfTracks = 5;
    const trackHeight = 100 / numberOfTracks;

    function createCircleGroup(track) {
        const group = document.createElement('div');
        group.classList.add('circle-group');
        group.style.top = `${track * trackHeight + trackHeight / 2}%`;
        group.style.transform = 'translateY(-50%)';

        const circleCount = Math.floor(Math.random() * 3) + 4; // 4 to 6 circles
        for (let j = 0; j < circleCount; j++) {
            const circle = document.createElement('div');
            circle.classList.add('circle');
            circle.style.backgroundColor = blueShades[Math.floor(Math.random() * blueShades.length)];
            group.appendChild(circle);
        }

        backgroundAnimation.appendChild(group);

        setTimeout(() => {
            group.remove();
        }, 20000);
    }

    function createNewGroup() {
        const availableTracks = Array.from({length: numberOfTracks}, (_, i) => i);
        const track = availableTracks[Math.floor(Math.random() * availableTracks.length)];
        createCircleGroup(track);
    }

    for (let i = 0; i < numberOfTracks; i++) {
        setTimeout(() => createCircleGroup(i), i * 2000);
    }

    setInterval(createNewGroup, 4000);
});


