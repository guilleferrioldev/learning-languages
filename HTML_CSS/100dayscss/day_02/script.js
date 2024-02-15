const Menu = document.querySelector('.menu');
const lineTop = document.querySelector('.line-1');
const line = document.querySelector('.line-2');
const lineButtom = document.querySelector('.line-3');

Menu.addEventListener('click', ()=> {
   lineTop.classList.toggle("top");
   line.classList.toggle("centro");
   lineButtom.classList.toggle("buttom");
})