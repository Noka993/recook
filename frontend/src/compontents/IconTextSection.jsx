import '../assets/iconTextSection.css'

function IconTextSection(props) {
    return (
        <div className="icon-text-section">
            <img src={props.icon} alt="icon" />
            {props.text}
        </div>
    )
}
export default IconTextSection