document.addEventListener("DOMContentLoaded", () => {
    let form = document.querySelector('.boxseats__form');
    let submitButton = form.querySelector('.boxseats__submit');
    let submitButtonLabel = submitButton.querySelector('.boxseats__submit--label');
    let loadingIndicator = submitButton.querySelector('.boxseats__submit--indicator');

    submitButton.addEventListener('mouseup', (event) => {
        form.submit()
        submitButton.setAttribute('disabled','disabled');
        submitButtonLabel.textContent = 'Loading...';
        loadingIndicator.classList.remove('d-none');
    });
});