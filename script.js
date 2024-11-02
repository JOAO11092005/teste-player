document.getElementById('loadVideo').addEventListener('click', function() {
    const videoUrl = document.getElementById('videoUrl').value;
    const videoPlayer = document.getElementById('videoPlayer');
    const videoSource = document.getElementById('videoSource');
    const statusMessage = document.getElementById('statusMessage');

    // Verifica se a URL começa com "http://"
    if (videoUrl.startsWith('http://')) {
        videoSource.src = videoUrl;
        videoPlayer.load(); // Recarrega o vídeo com a nova fonte
        videoPlayer.play(); // Inicia a reprodução
        statusMessage.textContent = ""; // Limpa mensagens anteriores
    } else {
        statusMessage.textContent = 'Por favor, insira uma URL válida que comece com "http://".';
    }
});

// Carregar o vídeo padrão ao abrir a página
window.onload = function() {
    const defaultVideoUrl = "http://cdn.teambr.live:80/movie/iptv0887/19971460887/49856.mp4";
    document.getElementById('videoSource').src = defaultVideoUrl;
    document.getElementById('videoPlayer').load();
};
