import { Home } from '../pages/pagesIndex'
import './homeBackground.css'

function HomeBackground() {
    return (
        <div className="home-background">
            <div className="opacity-layer">
                <div className="text-main">RECOOK</div>
                <div className="divider"></div>
                <div className="text-secondary">A PLACE TO SHARE YOUR TASTE. RECOOK IS A RECIPE SHARING PLATFORM</div>
            </div>
            <button className="discover">DISCOVER</button>
        </div>
    )
}
export default HomeBackground