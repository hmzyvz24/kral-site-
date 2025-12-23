from flask import Flask

app = Flask(__name__)

monthly_forecast = """
<p style="font-size:14px; line-height:1.4;">
<b>1 Aylık Tahmin (Aralık 2025 - Ocak 2026):</b><br>
• 22-31 Aralık: 8-12°C, sık yağmur<br>
• Yılbaşı: Kar ihtimali yüksek<br>
• Ocak başı: 4-9°C, karlı günler mümkün<br>
Kaynak: AccuWeather
</p>
"""

@app.route('/')
def ana_sayfa():
    return f"""
    <html>
    <head>
        <title>Kral Site</title>
        <meta name="google-site-verification" content="5V83CDxeEdCKTcIDpNrnb05zFAYpj6BlIEgrxW2M6sQ" />
        <style>
            body {{ font-family: 'Arial Black', Arial; text-align: center; background-image: url('https://i.pinimg.com/736x/68/fc/52/68fc522a8deaea59e9a1543df5380608.jpg'); background-size: cover; background-attachment: fixed; color: white; margin: 0; padding: 50px; }}
            h1, p, a, span {{ font-style: italic; text-shadow: 2px 2px 8px black; }}
            h1 {{ font-size: 70px; animation: glow 2s infinite; }}
            @keyframes glow {{ 0% {{ text-shadow: 0 0 20px yellow; }} 50% {{ text-shadow: 0 0 40px yellow; }} 100% {{ text-shadow: 0 0 20px yellow; }} }}
            .hava {{ position: absolute; top: 10px; left: 10px; background: rgba(0,0,0,0.7); padding: 8px; border-radius: 8px; font-size: 12px; cursor: pointer; width: 180px; }}
            .hava:hover {{ background: rgba(0,0,0,0.9); }}
            #detay {{ display: none; }}
            nav a {{ color: lime; font-size: 30px; margin: 30px; text-decoration: none; }}
        </style>
        <script>
            function toggleDetay() {{
                var d = document.getElementById('detay');
                d.style.display = (d.style.display === 'none') ? 'block' : 'none';
            }}
        </script>
    </head>
    <body>
        <div class="hava" onclick="toggleDetay()">
            <b>AccuWeather İstanbul</b><br>
            Şu an: ~12°C Bulutlu<br>
            Bugün: Yağmur<br>
            <i>Tıkla → 1 aylık</i>
            <div id="detay">{monthly_forecast}</div>
        </div>
        <h1>Hoşgeldin Kral/Kraliçe 👑</h1>
        <nav>
    <a href="/hakkinda">Hakkımda</a> |
    <a href="/iletisim">İletişim</a> |
    <a href="/hesap-makinesi">Hesap Makinesi</a> |
    <a href="/flappy-bird">Flappy Bird</a> |
    <a href="/xox">XOX</a>
    <a href="/yilan">Yılan</a>
</nav>
    </body>
    </html>
    """

@app.route('/hakkinda')
def hakkinda():
    return """
    <html><head><title>Hakkımda</title><style>
        body { background-image: url('https://i.pinimg.com/736x/68/fc/52/68fc522a8deaea59e9a1543df5380608.jpg'); background-size: cover; color: white; text-align: center; padding: 100px; }
        h1, p, a { font-style: italic; text-shadow: 2px 2px 8px black; }
    </style></head>
    <body>
        <h1>Hakkımda</h1>
        <p style="font-size: 25px;">Ben 14 yaşında bir yazılım mühendisiyim, ailem çok tatlıdır, Python'a ve Grok'a saygılarımla ❤️</p>
        <a href="/" style="color: lime; font-size: 30px;">Ana Sayfa</a>
    </body></html>
    """

@app.route('/iletisim')
def iletisim():
    return """
    <html><head><title>İletişim</title><style>
        body { background-image: url('https://i.pinimg.com/736x/68/fc/52/68fc522a8deaea59e9a1543df5380608.jpg'); background-size: cover; color: white; text-align: center; padding: 100px; }
        h1, p, a, span { font-style: italic; text-shadow: 2px 2px 8px black; }
    </style></head>
    <body>
        <h1>İletişim</h1>
        <p style="font-size: 25px;">Bana Instagram'dan ulaş!</p>
        <a href="https://instagram.com/h2m2za24">
            <img src="https://www.freeiconspng.com/uploads/new-instagram-icon-2.jpg" width="120" alt="Instagram">
            <br><span style="font-size: 35px; color: lime;">h2m2za24</span>
        </a>
        <br><br><a href="/" style="color: lime; font-size: 30px;">Ana Sayfa</a>
    </body></html>
    """

@app.route('/hesap-makinesi')
def hesap_makinesi():
    return """
    <html><head><title>Hesap Makinesi</title><style>
        body { background-image: url('https://i.pinimg.com/736x/68/fc/52/68fc522a8deaea59e9a1543df5380608.jpg'); background-size: cover; color: white; text-align: center; padding: 50px; }
        h1, button { font-style: italic; text-shadow: 2px 2px 8px black; }
    </style></head>
    <body>
        <h1>Hesap Makinesi</h1>
        <input type="text" id="sonuc" style="width:300px; height:50px; font-size:30px;"><br><br>
        <button onclick="ekle('7')">7</button><button onclick="ekle('8')">8</button><button onclick="ekle('9')">9</button><button onclick="ekle('/')">/</button><br>
        <button onclick="ekle('4')">4</button><button onclick="ekle('5')">5</button><button onclick="ekle('6')">6</button><button onclick="ekle('*')">*</button><br>
        <button onclick="ekle('1')">1</button><button onclick="ekle('2')">2</button><button onclick="ekle('3')">3</button><button onclick="ekle('-')">-</button><br>
        <button onclick="ekle('0')">0</button><button onclick="ekle('.')">.</button><button onclick="hesapla()">=</button><button onclick="ekle('+')">+</button><br><br>
        <button onclick="temizle()">Temizle</button>
        <script>
            function ekle(d) { document.getElementById('sonuc').value += d; }
            function hesapla() { try { document.getElementById('sonuc').value = eval(document.getElementById('sonuc').value); } catch(e) { alert('Hata'); } }
            function temizle() { document.getElementById('sonuc').value = ''; }
        </script>
        <br><a href="/" style="color: lime; font-size: 30px;">Ana Sayfa</a>
    </body></html>
    """

@app.route('/flappy-bird')
def flappy_bird():
    return """
    <html><head><title>Flappy Bird</title><style>
        body { background-image: url('https://i.pinimg.com/736x/68/fc/52/68fc522a8deaea59e9a1543df5380608.jpg'); background-size: cover; text-align: center; padding-top: 20px; }
        h1, p { color: white; font-style: italic; text-shadow: 2px 2px 8px black; }
        canvas { background: skyblue; border: 5px solid lime; }
    </style></head>
    <body>
        <h1>Flappy Bird Oyunu</h1>
        <canvas id="canvas" width="400" height="600"></canvas>
        <p id="talimat" style="font-size: 20px;">Boşluk tuşuna basarak zıpla!</p>
        <script>
            const canvas = document.getElementById('canvas');
            const ctx = canvas.getContext('2d');
            let birdY = 300;
            let velocity = 0;
            let pipes = [];
            let score = 0;
            let gameOver = false;

            function resetGame() {
                birdY = 300;
                velocity = 0;
                pipes = [];
                score = 0;
                gameOver = false;
                document.getElementById('talimat').innerText = 'Boşluk tuşuna basarak zıpla!';
            }

            function draw() {
                ctx.clearRect(0, 0, 400, 600);
                velocity += 0.4;
                birdY += velocity;
                ctx.fillStyle = 'yellow';
                ctx.fillRect(50, birdY, 40, 40); // Kuş

                if (birdY > 560 || birdY < 0) gameOver = true;

                if (pipes.length === 0 || pipes[pipes.length - 1].x < 250) {
                    let gap = Math.random() * 200 + 100;
                    pipes.push({x: 400, gap: gap, passed: false});
                }

                pipes.forEach(pipe => {
                    pipe.x -= 3;
                    ctx.fillStyle = 'green';
                    ctx.fillRect(pipe.x, 0, 60, pipe.gap);
                    ctx.fillRect(pipe.x, pipe.gap + 200, 60, 400);

                    if (pipe.x < 90 && pipe.x > 10 && (birdY < pipe.gap || birdY + 40 > pipe.gap + 200)) {
                        gameOver = true;
                    }

                    if (pipe.x < 50 && !pipe.passed) {
                        pipe.passed = true;
                        score++;
                    }
                });

                pipes = pipes.filter(pipe => pipe.x > -60);

                ctx.fillStyle = 'white';
                ctx.font = 'bold 35px Arial';
                ctx.fillText('Puan: ' + score, 120, 50);

                if (gameOver) {
                    ctx.fillStyle = 'red';
                    ctx.font = 'bold 40px Arial';
                    ctx.fillText('OYUN BİTTİ!', 70, 280);
                    ctx.fillStyle = 'white';
                    ctx.fillText('Puanın: ' + score, 100, 330);
                    ctx.fillText('SPACE ile Yeniden Başla!', 30, 380);
                    document.getElementById('talimat').innerText = 'SPACE ile yeniden başla!';
                    return;
                }

                requestAnimationFrame(draw);
            }

            document.addEventListener('keydown', (e) => {
                if (e.key === ' ') {
                    if (gameOver) {
                        resetGame();
                        draw();
                    } else {
                        velocity = -10;
                    }
                }
            });

            resetGame();
            draw();
        </script>
        <br><a href="/" style="color: lime; font-size: 30px;">Ana Sayfa</a>
    </body></html>
    """
@app.route('/xox')
def xox():
    return """
    <html>
    <head>
     @app.route('/xox')
def xox():
    return """
    <html>
    <head>
        <title>XOX</title>
        <style>
            body { background-image: url('https://i.pinimg.com/736x/68/fc/52/68fc522a8deaea59e9a1543df5380608.jpg'); background-size: cover; color: white; text-align: center; padding-top: 50px; font-family: Arial; }
            h1 { font-style: italic; text-shadow: 2px 2px 8px black; font-size: 60px; }
            #board { display: grid; grid-template-columns: repeat(3, 110px); gap: 10px; width: 350px; margin: 40px auto; }
            .cell { width: 110px; height: 110px; background: rgba(0,0,0,0.7); font-size: 70px; color: lime; cursor: pointer; border: 4px solid lime; display: flex; align-items: center; justify-content: center; border-radius: 10px; }
            .cell:hover { background: rgba(0,0,0,0.9); }
            #message { font-size: 60px; margin: 40px; font-weight: bold; animation: pulse 1s infinite; }
            @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.1); } 100% { transform: scale(1); } }
            button { padding: 15px 30px; font-size: 25px; background: lime; color: black; border: none; cursor: pointer; border-radius: 10px; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>XOX</h1>
        <p style="font-size: 35px;">Sıra: <span id="turn">X</span></p>
        <div id="board"></div>
        <div id="message"></div>
        <button onclick="resetGame()">Yeni Oyun</button>
        <script>
            const board = document.getElementById('board');
            const cells = [];
            let currentPlayer = 'X';
            let gameActive = true;
            let gameState = ["", "", "", "", "", "", "", "", ""];

            const winningConditions = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]
            ];

            function createBoard() {
                board.innerHTML = '';
                for (let i = 0; i < 9; i++) {
                    const cell = document.createElement('div');
                    cell.classList.add('cell');
                    cell.addEventListener('click', () => handleCellClick(i));
                    board.appendChild(cell);
                    cells.push(cell);
                }
            }

            function handleCellClick(index) {
                if (gameState[index] !== "" || !gameActive) return;
                gameState[index] = currentPlayer;
                cells[index].innerText = currentPlayer;

                if (checkWinner()) {
                    document.getElementById('message').innerHTML = `<span style="color: ${currentPlayer === 'X' ? 'cyan' : 'magenta'};">${currentPlayer} KAZANDI! 👑</span>`;
                    gameActive = false;
                } else if (gameState.every(cell => cell !== "")) {
                    document.getElementById('message').innerHTML = '<span style="color: yellow;">BERABERE!</span>';
                    gameActive = false;
                } else {
                    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
                    document.getElementById('turn').innerText = currentPlayer;
                }
            }

            function checkWinner() {
                return winningConditions.some(condition => {
                    return condition.every(index => gameState[index] === currentPlayer);
                });
            }

            function resetGame() {
                gameState = ["", "", "", "", "", "", "", "", ""];
                currentPlayer = 'X';
                gameActive = true;
                document.getElementById('turn').innerText = 'X';
                document.getElementById('message').innerHTML = '';
                createBoard();
            }

            createBoard();
        </script>
        <br><br><a href="/" style="color: lime; font-size: 30px;">Ana Sayfa</a>
    </body>
    </html>
    """
    @app.route('/yilan')
def yilan():
    return """
    <html>
    <head>
        <title>Yılan</title>
        <style>
            body { background-image: url('https://i.pinimg.com/736x/68/fc/52/68fc522a8deaea59e9a1543df5380608.jpg'); background-size: cover; color: white; text-align: center; padding-top: 20px; font-family: Arial; }
            h1 { font-style: italic; text-shadow: 2px 2px 8px black; font-size: 60px; }
            canvas { background: rgba(0,0,0,0.5); border: 5px solid lime; border-radius: 10px; }
            #score { font-size: 35px; margin: 20px; font-style: italic; text-shadow: 2px 2px 8px black; }
            button { padding: 15px 30px; font-size: 25px; background: lime; color: black; border: none; cursor: pointer; border-radius: 10px; margin-top: 20px; }
            p { font-size: 25px; }
        </style>
    </head>
    <body>
        <h1>Yılan</h1>
        <p>Ok tuşları veya WASD ile hareket et!</p>
        <canvas id="canvas" width="400" height="400"></canvas>
        <div id="score">Skor: 0</div>
        <button onclick="resetGame()">Yeni Oyun</button>
        <script>
            const canvas = document.getElementById('canvas');
            const ctx = canvas.getContext('2d');
            const gridSize = 20;
            const tileCount = canvas.width / gridSize;

            let snake = [
                {x: 10, y: 10}
            ];
            let food = {};
            let dx = 0;
            let dy = 0;
            let score = 0;
            let gameOver = false;

            function randomFood() {
                food = {
                    x: Math.floor(Math.random() * tileCount),
                    y: Math.floor(Math.random() * tileCount)
                };
            }

            function drawGame() {
                ctx.fillStyle = 'rgba(0,0,0,0.8)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                // Yılan
                ctx.fillStyle = 'lime';
                snake.forEach((part, index) => {
                    ctx.fillRect(part.x * gridSize, part.y * gridSize, gridSize - 2, gridSize - 2);
                    if (index === 0) ctx.fillStyle = 'yellow'; // Kafa sarı
                });

                // Yem
                ctx.fillStyle = 'red';
                ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize - 2, gridSize - 2);

                // Skor
                document.getElementById('score').innerText = 'Skor: ' + score;
            }

            function update() {
                if (gameOver) return;

                const head = {x: snake[0].x + dx, y: snake[0].y + dy};

                // Duvar çarpışma
                if (head.x < 0 || head.x >= tileCount || head.y < 0 || head.y >= tileCount) {
                    gameOver = true;
                    document.getElementById('score').innerText = 'Oyun Bitti! Skor: ' + score;
                    return;
                }

                // Kendine çarpışma
                for (let part of snake) {
                    if (head.x === part.x && head.y === part.y) {
                        gameOver = true;
                        document.getElementById('score').innerText = 'Oyun Bitti! Skor: ' + score;
                        return;
                    }
                }

                snake.unshift(head);

                // Yem yeme
                if (head.x === food.x && head.y === food.y) {
                    score++;
                    randomFood();
                } else {
                    snake.pop();
                }

                drawGame();
            }

            function changeDirection(event) {
                const LEFT = 37;
                const RIGHT = 39;
                const UP = 38;
                const DOWN = 40;
                const W = 87;
                const A = 65;
                const S = 83;
                const D = 68;

                const key = event.keyCode;
                if (key === LEFT || key === A) {
                    if (dx !== 1) { dx = -1; dy = 0; }
                } else if (key === RIGHT || key === D) {
                    if (dx !== -1) { dx = 1; dy = 0; }
                } else if (key === UP || key === W) {
                    if (dy !== 1) { dx = 0; dy = -1; }
                } else if (key === DOWN || key === S) {
                    if (dy !== -1) { dx = 0; dy = 1; }
                }
            }

            function resetGame() {
                snake = [{x: 10, y: 10}];
                dx = 0;
                dy = 0;
                score = 0;
                gameOver = false;
                randomFood();
                drawGame();
            }

            document.addEventListener('keydown', changeDirection);
            randomFood();
            setInterval(update, 150);
        </script>
        <br><br><a href="/" style="color: lime; font-size: 30px;">Ana Sayfa</a>
    </body>
    </html>
    """
if __name__ == '__main__':
    app.run(debug=True)
