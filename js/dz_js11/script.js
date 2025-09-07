class Header{
    constructor(img){
        this.src = img
        this.out = ``
    }

    render(id){
        this.out = `
        <img src ="${this.src}" alt="">
        `
        document.querySelector(`#${id}`).innerHTML = this.out
    }
}

class HeaderExt extends Header{
    constructor(img, text){
        super(img)
        this.text = text
    }

    render(id){
        super.render(id)
        this.out += `
        <h3>${this.text}</h3>
        `
        document.querySelector(`#${id}`).innerHTML = this.out
    }
}

let img = `https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/233_Node_Js_logo-128.png`
let header = new HeaderExt(img, 'Работа 24 часа в сутки, 7дней')
header.render('header1')

let img2 = `https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-128.png`
let header2 = new HeaderExt(img2, 'Нет географических границ')
header2.render('header2')

let img3 = `https://cdn3.iconfinder.com/data/icons/web-technologies-1/154/js-javascript-monitor-pc-page-web-dynamic-128.png`
let header3 = new HeaderExt(img3, 'Ассортимент')
header3.render('header3')

let img4 = `https://img.icons8.com/?size=160&id=0Da6k7SMq0hs&format=png`
let header4 = new HeaderExt(img4, 'React')
header4.render('header4')

let img5 = `https://img.icons8.com/?size=128&id=lVitPDXqQKP8&format=png`
let header5 = new HeaderExt(img5, "JavaScript")
header5.render('header5')

let img6 = `https://img.icons8.com/?size=96&id=13441&format=png`
let header6 = new HeaderExt(img6, "Python")
header6.render('header6')

let img7 = `https://icons8.com/icon/IuuVVwsdTi2v/external-django-a-high-level-python-web-framework-that-encourages-rapid-development-logo-filled-tal-revivo`
let header7 = new HeaderExt(img6, "Django")
header7.render('header7')

let img8 = `https://icons8.com/icon/VMRAbKfEzssG/sqlite`
let header8 = new HeaderExt(img6, "SQLite")
header8.render('header8')

let img9 = `https://icons8.com/icon/2572/java-coffee-cup-logo`
let header9 = new HeaderExt(img6, "Java")
header9.render('header9')

