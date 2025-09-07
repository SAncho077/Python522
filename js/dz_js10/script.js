function User(name, age, job){
    this.name = name
    this.age = age
    this.job = job

    this.who = function(){
        document.writeln("Я " + this.name + " мне " + this.age + ' лет. '+ "Я работаю " + this.job + 'ом' + '<br>')
    }
}

let Person = new User("Дмитрий", 26, "Дизайнер")
Person.who()
let Person1 = new User("Станислав", 29, "Программист")
let Person2 = new User("Сергей", 35, "Менеджер")
Person1.who()
Person2.who()