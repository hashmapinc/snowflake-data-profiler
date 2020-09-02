import React, {Component} from 'react';
import hashmaplogo from './hashmap_banner_white.png';
import '../main.css'

class Navbar extends Component {
    render() {
        return (
        <header className="navbar navbar-expand-lg navbar-dark fixed-top bg-dark">
            <a className="navbar-brand" href="https://www.hashmapinc.com/" target="_blank">
                {<img src={hashmaplogo} width="200px"/>}
            </a>

            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>

            <div className="collapse navbar-collapse" id="navbarNav">
                <div className="mx-auto my-2 text-white">
                    <h3>Snowflake Data Profiler</h3>
                </div>

                <ul className="navbar-nav">
                    <li className="nav-item">
                    <a className="nav-link" href="https://www.hashmapinc.com/snowflakedataprofiler-reachout" target="_blank">Contact
                        Us</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="https://forms.gle/WfiB6YctX5Jg2zTs6" target="_blank">Feedback </a>
                    </li>
                    <li className="nav-item">
                        <a href={''} target="_blank" className="nav-item btn btn-primary ml-3">
                        See a Sample Profile
                        </a>
                    </li>
                </ul>
            </div>
        </header>
        )
    }
}

export default Navbar

    