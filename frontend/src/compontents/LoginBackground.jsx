import '../assets/loginBackground.css'
import Button from './Button'
import Divider from './Divider'
import SectionHeader from './HeaderBackground'
import InputField from './InputField'
function loginBackground() {
    return (
        <div className="login-section">
            <SectionHeader text="LOGIN" />
            <div className="login-form">
                <InputField type="text" placeholder="USERNAME" />
                <InputField type="password" placeholder="PASSWORD" />
                <Button id="login-button" link="/recipes" text="LOG IN" />
                <Divider />
                <a href='/register' id="register-link">Don't have an account? Register</a>
            </div>
        </div>
    )
}
export default loginBackground
