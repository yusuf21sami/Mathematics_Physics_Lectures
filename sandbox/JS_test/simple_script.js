const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const wallX = 100; // X-owa pozycja ściany
const springLength = 200; // Długość sprężyny w stanie spoczynku
const springWidth = 20; // Szerokość sprężyny
const amplitude = 100; // Amplituda drgań
const ballRadius = 20; // Promień kulki
const numCoils = 10; // Liczba zwojów sprężyny

let time = 0; // Czas do symulacji ruchu

function drawSpringAndBall() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Oscylacyjna pozycja kulki
    const ballX = wallX + springLength + amplitude * Math.sin(time);
    const ballY = canvas.height / 2;

    // Rysowanie ściany
    ctx.fillStyle = 'gray';
    ctx.fillRect(wallX - 20, ballY - 50, 20, 100);

    // Rysowanie sprężyny
    ctx.beginPath();
    ctx.moveTo(wallX, ballY);
    for (let i = 0; i <= numCoils; i++) {
        const x = wallX + (springLength / numCoils) * i + amplitude * Math.sin(time) * (i / numCoils);
        const y = ballY + springWidth * (i % 2 === 0 ? 1 : -1);
        ctx.lineTo(x, y);
    }
    ctx.lineTo(ballX - ballRadius, ballY);
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Rysowanie kulki
    ctx.beginPath();
    ctx.arc(ballX, ballY, ballRadius, 0, Math.PI * 2);
    ctx.fillStyle = 'red';
    ctx.fill();

    time += 0.05; // Zwiększanie czasu dla animacji
    requestAnimationFrame(drawSpringAndBall);
}

drawSpringAndBall();
