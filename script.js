// Este arquivo pode ser utilizado para adicionar funcionalidades adicionais ao player
document.addEventListener('DOMContentLoaded', function() {
    const video = document.getElementById('my-video');
    
    video.addEventListener('error', function() {
        console.error('Erro ao tentar reproduzir o vídeo: ', video.error);
        alert('Ocorreu um erro ao tentar reproduzir o vídeo. Verifique o link.');
    });
});
