// Скрипт sample.js
/********************************
Здесь некоторые элементы языка
подробнее здесь: https://learn.javascript.ru
********************************/
// Массивы
let colors = ["Красный", "Синий", "Голубой"]

document.writeln("<h1>Цвета:</h1><ol>");
// Цикл for
for(let i=0; i<colors.length; i++) {
    document.writeln("<li>" + colors[i] + "</li>");
}
document.writeln("</ol>")

// Функция
function sayHello(name) {
    document.writeln("Вас зовут " + name);
}
//
//// Переменная (var или let)
/* let name = prompt("Ваше имя: ");
sayHello(name); // вызов функции  */

