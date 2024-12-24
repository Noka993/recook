import './header.css'

function Header() {
    return (
        <div className="nav-bar">
            <div className="menu-logo">
                <p className="logo-text">RECOOK</p>
            </div>
            <div className="menu">
                <div className="menu-item">ABOUT</div>
                <div className="menu-item">CONTACT</div>
                <div className="menu-item">SIGN IN</div>
                <div className="menu-item">LOGIN</div>
            </div>
        </div>
    )
}
export default Header