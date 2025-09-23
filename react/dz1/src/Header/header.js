import './header.css'
function Header(props) {
    let { nav, db, name } = props
    return (
        <div className="container">
            <div className="header-box">
                <div className="header-logo">
                    <h1>{name}</h1>
                    <p>Мои сериалы</p>
                </div>

                <div className="header-controls">
                    <a href="#">Вход и регистрация</a>
                </div>
            </div>
        </div>
                )
}

export default Header
