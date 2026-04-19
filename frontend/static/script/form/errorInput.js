function showError(inputElement) {
    inputElement.classList.remove('input-error');
    void inputElement.offsetWidth; // перезапуск анимации
    inputElement.classList.add('input-error');
    
    // убрать класс после анимации
    setTimeout(() => {
        inputElement.classList.remove('input-error');
    }, 3000);
}
