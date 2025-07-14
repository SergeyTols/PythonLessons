// получить доступ к кнопке
const topBtn = document.querySelector(".go-top");
// скролинг окна
window.addEventListener("scroll", trackScroll);
// реакция на нажатие
window.addEventListener("click", goTop);

function trackScroll() {
    // положение скроллинга от верхушки окна
    const scrolled = window.pageYOffset;
    // высота окна браузера
    const wh = document.documentElement.clientHeight
    console.log(wh);
    // в прокрутке вышли за пределы одного экрана
    if(scrolled > wh) {
    // должна показаться кнопка
        //topBtn.classList.add("go-top--show");
        topBtn.style.display = 'block'
    } else {
    // или изчезает
        //topBtn.classList.remove("go-top--show");
        topBtn.style.display = 'none';
    }
}

function goTop() {
    // пока не дошли до верха
    if (window.pageYOffset > 0) {
        // скролинг к верху
        window.scrollBy(0, -500); // по Y на 28px
        setTimeout(goTop, 0); // рекурсивный вызов самой себя через задержку
    }
}