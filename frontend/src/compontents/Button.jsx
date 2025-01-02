import './button.css'

function Button(props) {
    return (
            <button className="btn-default" id={props.id}><a href={props.link}>{props.text}</a></button>
    )
}
export default Button