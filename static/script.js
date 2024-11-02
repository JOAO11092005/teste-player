document.getElementById('check-button').addEventListener('click', function() {
    var videoUrl = document.getElementById('video-url').value;
    var videoPlayer = videojs('video-player');
    var message = document.getElementById('message');

    videoPlayer.src({ type: 'video/mp4', src: videoUrl });
    
    // Testar se o vídeo pode ser reproduzido
    videoPlayer.ready(function() {
        this.on('error', function() {
            message.textContent = "Erro ao carregar o vídeo. Verifique o link ou o formato.";
        });

        this.on('loadedmetadata', function() {
            message.textContent = "Vídeo carregado com sucesso!";
            this.play().catch(function(error) {
                message.textContent = "Não foi possível reproduzir o vídeo automaticamente. Clique no player para reproduzir.";
            });
        });
    });

    videoPlayer.show();
});
