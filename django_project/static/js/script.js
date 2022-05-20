const counterNode = document.querySelector('.product-view__counter');
const incBtnNode = document.querySelector('.js-inc-btn')
const clearBtnNode = document.querySelector('.js-clear-btn')
let counter = 0;

counterNode.innerText = counter;

incBtnNode.addEventListener('click', () => {
    counter += 1;
    counterNode.innerText = counter;
});

clearBtnNode.addEventListener('click', () => {
    counter -= 1;
    counterNode.innerText = counter;
});