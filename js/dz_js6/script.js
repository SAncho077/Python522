let array = new Array("2.jpg", '3.jpg', '4.jpg')
document.writeln("<img src='"+ array[0] +"'>")
document.writeln("<img src='"+ array[1] +"'>")
document.writeln("<img src='"+ array[2] +"'>" + "<br>" )

document.writeln("поменять ")
document.writeln("<input type='number' min='1' max='3' class='one'> " )
document.writeln("на ")
document.writeln("<input type='number' min='1' max='3' class='two'> " )
document.writeln("<input type='button' value='Поменять' class='btn'>")


let one = document.querySelector(".one")
let two = document.querySelector(".two")

let btn1 = document.querySelector(".btn")

btn1.addEventListener("click", function(){
    let value1 = document.querySelector(".one").value
    let value2 = document.querySelector(".two").value
    console.log(value1)
    console.log(value2)
    let index1 = value1 - 1
    let index2 = value2 - 1
    let images2 = array[2]
    let t = array[index1]
    array[index1] = array[index2]
    array[index2] = t

    let images = document.querySelectorAll('img')
    images[0].src = array[0]
    images[1].src = array[1]
    images[2].src = array[2]
})



