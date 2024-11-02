// Inicializa o player Video.js
const player = videojs('videoPlayer');

// Função para carregar o vídeo
function loadVideo(url) {
    const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
    const fullUrl = proxyUrl + url; // Adiciona o proxy à URL
    player.src({ type: 'video/mp4', src: fullUrl });
    player.play();
}

// Evento de clique para carregar o vídeo
document.getElementById('loadVideo').addEventListener('click', function() {
    const videoUrl = document.getElementById('videoUrl').value;
    const statusMessage = document.getElementById('statusMessage');

    if (videoUrl.startsWith('http://') || videoUrl.startsWith('https://')) {
        loadVideo(videoUrl);
        statusMessage.textContent = ""; // Limpa mensagens anteriores
    } else {
        statusMessage.textContent = 'Por favor, insira uma URL válida que comece com "http://" ou "https://".';
    }
});

// Evento de clique para verificar a URL
document.getElementById('checkUrl').addEventListener('click', function() {
    const videoUrl = document.getElementById('videoUrl').value;
    const statusMessage = document.getElementById('statusMessage');

    if (videoUrl.startsWith('http://') || videoUrl.startsWith('https://')) {
        fetch(videoUrl, { method: 'HEAD' })
            .then(response => {
                if (response.ok) {
                    statusMessage.textContent = 'URL está acessível e válida.';
                    loadVideo(videoUrl); // Carrega o vídeo se a URL for válida
                } else {
                    statusMessage.textContent = 'A URL não está acessível. Código: ' + response.status;
                }
            })
            .catch(error => {
                statusMessage.textContent = 'Erro ao verificar a URL: ' + error.message;
            });
    } else {
        statusMessage.textContent = 'Por favor, insira uma URL válida que comece com "http://" ou "https://".';
    }
});
