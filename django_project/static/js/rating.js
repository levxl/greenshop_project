const rating = document.querySelector('form[name=rating]');

rating.addEventListener('change', function(){
    let data = new FormData(this);
    fetch(`${this.action}`, {
        method : 'POST',
        body : data
    })
    .then(response => alert("Рейтинг устоновлен"))
    .catch(error => alert("Ошибка"))
})
