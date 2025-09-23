import './nav.css'

function Nav(props){
    let {nav} = props
    return (
        <nav>
            <ul>
                {
                    Object.keys(props.nav).map(elem => {
                        return <li key={elem}>
                            <a href={nav.elem}>{elem}</a>
                        </li>
                    })
                }
            </ul>
        </nav>
    )
}

export default Nav