import '../assets/sectionHeader.css'

function SectionHeader(props) {
    return (
        <div className="section-header">
            {props.text}
        </div>
    )
}
export default SectionHeader