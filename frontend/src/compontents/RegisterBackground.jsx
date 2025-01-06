import '../assets/registerBackground.css'
import Button from './Button'
import Divider from './Divider'
import HeaderBackground from './HeaderBackground'
import InputField from './InputField'
function registerBackground() {
    return (
        <div className="register-section">
            <HeaderBackground text="SIGN UP" />
            <div className="register-form">
                <InputField type="text" placeholder="USERNAME" />
                <InputField type="password" placeholder="PASSWORD" />
                <InputField type="password" placeholder="CONFIRM PASSWORD" />
                <Button id="register-button" link="/recipes" text="SIGN UP" />
                <Divider />
                <a href='/login' id="login-link">Already have an account? Login</a>
            </div>
        </div>
    )
}
export default registerBackground
