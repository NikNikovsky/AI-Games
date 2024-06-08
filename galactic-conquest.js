const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const galaxySize = 1000;
const numPlanets = 50;
const planets = [];
const fleets = [];

class Planet {
    constructor(x, y, size, owner) {
        this.x = x;
        this.y = y;
        this.size = size;
        this.owner = owner;
        this.resources = Math.floor(Math.random() * 100);
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = this.owner ? 'blue' : 'gray';
        ctx.fill();
        ctx.closePath();
    }
}

class Fleet {
    constructor(x, y, targetX, targetY, owner) {
        this.x = x;
        this.y = y;
        this.targetX = targetX;
        this.targetY = targetY;
        this.owner = owner;
        this.size = 5;
    }

    update() {
        const dx = this.targetX - this.x;
        const dy = this.targetY - this.y;
        const distance = Math.sqrt(dx * dx + dy * dy);
        if (distance > 1) {
            this.x += dx / distance;
            this.y += dy / distance;
        } else {
            // Fleet has reached its destination
        }
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = this.owner ? 'blue' : 'red';
        ctx.fill();
        ctx.closePath();
    }
}

function generateGalaxy() {
    for (let i = 0; i < numPlanets; i++) {
        const x = Math.random() * galaxySize;
        const y = Math.random() * galaxySize;
        const size = Math.random() * 20 + 10;
        const owner = null;
        planets.push(new Planet(x, y, size, owner));
    }
}

function drawGalaxy() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    planets.forEach(planet => planet.draw());
    fleets.forEach(fleet => fleet.draw());
}

function updateGame() {
    fleets.forEach(fleet => fleet.update());
    drawGalaxy();
    requestAnimationFrame(updateGame);
}

canvas.addEventListener('click', (event) => {
    const x = event.clientX;
    const y = event.clientY;
    fleets.push(new Fleet(canvas.width / 2, canvas.height / 2, x, y, 'player'));
});

generateGalaxy();
updateGame();
