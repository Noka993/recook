import Divider from './Divider'
import './homeBackground.css'

function HomeBackground() {
    return (
        <div className="home-background">
            <div className="opacity-layer">
                <div className="text-main">RECOOK</div>
                <Divider />
                <div className="text-secondary">A PLACE TO SHARE YOUR TASTE. RECOOK IS A RECIPE SHARING PLATFORM</div>
            </div>
            <button className="discover"><a href="/recipes" id="discover">DISCOVER</a></button>
        </div>
    )
}
export default HomeBackground