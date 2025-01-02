import './loginBackground.css'
import Button from './Button'
import Divider from './Divider'
function loginBackground() {
    return (
        <div className="login-section">
            <div className="login-header">LOGIN</div>
            <div className="login-form">
                <input type="text" placeholder="USERNAME" />
                <input type="password" placeholder="PASSWORD" />
                <Button id="login-button" link="/recipes" text="LOG IN" />
                <Divider />
            </div>
        </div>
    )
}
export default loginBackground
