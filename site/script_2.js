    var windowButton = document.getElementById('window-button');
    var header = document.getElementById('download-text');
    var i = 1
    windowButton.addEventListener('click', () => {
        if (i == 1){
            header.textContent = 'Спасибо за скачивание';
        }
        else header.textContent = 'Спасибо за скачивание ' + i + ' раз';
        i++
    });