"use strict"

// let message; // let. const, var
// message = "Hello";
// console.log(message);

// let a = 10;
// a = 3.5;

// let b, c;
// let d = 5, e = 2;

// let firstName = "Irina";
// console.log(firstName)

// const week = 7;

// let str1 = "Двойные кавычки";
// let str2 = "Одинарные кавычки";
// let str3 = `Обратные ${str1} и ${str2}
//     кав ыч  ки`;

// console.log(str1);
// console.log(str2);
// console.log(str3);

// let firstName = "Иван";
// alert(`Hello ${firstName}`);

// let one = "365"
// let two = "Земля"
// let three = "7 млрд"
// let four  = "Солнца"

// alert(`Мы живем на планете ${two}, она делает один оборот вокруг ${four} за ${one} дней. Население нашей планеты составляет примерно ${three} человек`)

// let res = confirm("Знаете ли вы HTML?");
// console.log(res) // ОК => true Отмена => false

// if(res){
//     alert("Пора учить JavaScript");} 
// else {
//     alert("Нужно выучить");
// }

//  Типы данных
//  - number
//  - string
//  - boolean
//  - null (object)
//  - undefined

// - Object

// let number = 13;
// console.log(number, typeof number);
// console.log(number, typeof(number));

// let a = 23.56
// console.log(a, typeof(a));

// let b = "Hello"
// console.log(b, typeof(b))

// let c = true
// console.log(c, typeof(c))

// let d = null;
// console.log(d, typeof(d));

// let e = undefined;
// console.log(e, typeof(e))


// let res = prompt("Ваше имя", "Значение по умолчанию");
// console.log(res); // OK => string, Отмена => Null

// let a = 12
// let b = 8

// console.log('+', a + b);
// console.log('-', a - b);
// console.log('*', a * b);
// console.log('/', a / b);
// console.log('%', a % b);
// console.log('**', a % b);


// let a = "Hello";
// let b = "World";
// console.log(a + b);  

// let a = +prompt("Введите первое число: ");
// let b = parseInt(prompt("Введите второе число: "));
// alert("Результат: " + (a + b));


// console.log(parseInt("21.84")) // 21
// console.log(parseFloat("21.84")) // 21.84
// console.log(parseFloat("21.84123").toFixed(2)) // 21.84
// console.log(Number("21.84123")) // 21.84
// console.log(+"21.84123")


// let a = 0, b = 0;
// a++; // a += 1
// b--; // a -= 1
// console.log(a)
// console.log(b)


// let a = 0, b = 0;
// let c = a++ + 2;
// let d = ++b +2
// console.log(a)
// console.log(b)
// console.log(b)
// console.log(b)

// let a = 1;
// let b = a++; // b = 1, a = 2
// let c = b + 5 + a; // c = 1 + 5 + 2
// console.log(c)  

// a++ или a += 1 или a = a + 1

// let a = 1;
// let b = ++a; // b = 2, a = 2
// let c = b + 5 + a; // c = 2 + 5 + 2
// console.log(c)  

// let num = 10;
// num += 5
// console.log(num)

// num -= 7;
// console.log(num)

// console.log(5 > 3)
// console.log(5 == '5') True
// console.log(5 === '5') False

// 7 > 3 ? alert("7") : alert('-3')

// let ch = prompt("Угадайте число от 1 до 10");
// let num = 7;
// // (ch == num) ? alert("Угадали") : alert("Не угадали")
// (ch == num) ? alert("Угадали") : (ch < num) ? alert("Заданное число") : alert("Загаданное число меньше")

// if (Условие){
//     блок истина
// } else {
//     блок ложь
// }
// false => 0, 0.0, '', false, null, undefined, NaN



// a = null
// if (a){
//     console.log("True");
// } else {
//     console.log("False")
// } 


// let a = +prompt("Введите первое число: ");
// let b = parseInt(prompt("Введите второе число: "));

// if (b != 0)
//     alert(a / b); // infinity
// else
//     alert("На 0 делить нельзя")


// let a = 12;
// let b = 6;

// if (a > b){
//     alert(a + " >" + b)
// } 
// if(a < b) {
//     alert(a + ' < ' + b)
// }   
// if(a == b) {
//     alert(a + ' == ' + b)
// }

// if (a > b){
//     alert(a + " >" + b)
// } else {
//     alert(a + ' < ' + b)
// } 


// if (a > b){
//     alert(a + " >" + b)
// } 
// else if(a < b) {
//     alert(a + ' < ' + b)
// }   
// else(a == b) {
//     alert(a + ' == ' + b)
// }


// let login = prompt("Введите логин: ", "admin")
// if(login){
//     if(login == 'admin'){
//         let psw = prompt("Введите пароль");
//         if(psw){
//             if (psw == "password"){
//                 alert("Добро пожаловать")
//             } else {
//                 alert("Пароль не верен")
//             }
//         } else {
//             alert('Вход отменен');
//         }
//     } else {
//         alert("Я вас не знаю")
//     }
// } else {
//     alert("Вход отменен")
// }

// let a = 1;
// if (a){
//     let b = 5;
// }

// if (5 == 5 && 5 > 2){
//     console.log("TRUE")
// } else {
//     console.log("FALSE")
// }

// console.log(!9); // 9 => !true => False
// console.log(!0)
// console.log(!!"Hello")   

// let age = prompt("Введите возраст")
// if (age > 17 || age < 70){
//     alert("Вы можете получать права")
// } else {
//     alert("Права не давать ")  
// }

// let age = prompt("Введите возраст")
// if (age < 18 || age > 69){
//     alert("Права не давать ") 
// } else {
//     alert("Вы можете получать права")
// }  

// switch (условие){
//     case значение_1:
//         блок кода;
//         break;
//     case значение_n:
//         блок кода;
//         break;
//     default:
//         блок кода
//     }   

// let a = +prompt("Введите результат: ");
// switch(a){
//     case 1:
//         alert("Код 1")
//         break
//     case 2:
//         alert("Код 2")
//         break
//     case 3:
//         alert("Код 3")
//         break
//     default:
//         alert("Я таких значений не знаю")
//         break
// }

// let a = +prompt("Введите результат: '2 + 2': ");
// switch(a){
//     case 4:
//         alert("верно")
//         break
//     case 3:
//     case 5:
//         alert("Не верно")
//         break
//     default:
//         alert("Я таких значений не знаю")
//         break
// }

let m = +prompt("Введите номер месяца");
let n;
switch(m){
    case 1: n="Январь"; break
    case 2: n="Февраль"; break
    case 3: n="Март"; break
    case 4: n="Апрель"; break
    case 5: n="Май"; break
    case 6: n="Июнь"; break
    case 7: n="Июль"; break
    case 8: n="Август"; break
    case 9: n="Сентябрь"; break
    case 10: n="Октябрь"; break
    case 11: n="Ноябрь"; break
    case 12: n="Декабрь"; break
    default: n="Неправильный номер месяца"
}
alert("Вы ввели " + n)