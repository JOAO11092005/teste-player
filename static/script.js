document.getElementById('check-button').addEventListener('click', function() {
    const videoUrl = document.getElementById('video-url').value;
    const playerContainer = document.getElementById('player-container');
    const videoPlayer = document.getElementById('video-player');
    const videoSource = document.getElementById('video-source');
    const errorMessage = document.getElementById('error-message');

    // Limpar mensagens anteriores
    playerContainer.classList.add('hidden');
    errorMessage.classList.add('hidden');
    videoSource.src = '';

    fetch('/check-video', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: videoUrl })
    })
    .then(response => response.json())
    .then(data => {
        if (data.valid) {
            videoSource.src = data.url;
            videoPlayer.load();
            playerContainer.classList.remove('hidden');
        } else {
            errorMessage.textContent = 'Vídeo não encontrado ou URL inválido.';
            errorMessage.classList.remove('hidden');
        }
    })
    .catch(error => {
        errorMessage.textContent = 'Erro ao verificar o vídeo: ' + error;
        errorMessage.classList.remove('hidden');
    });
});
