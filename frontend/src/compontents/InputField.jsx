import '../assets/inputField.css'

function InputField(props) {
    return (
        <input className="input-field" type={props.type} placeholder={props.placeholder} />
    )
}
export default InputField