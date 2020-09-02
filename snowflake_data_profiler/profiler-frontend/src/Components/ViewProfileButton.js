import React, {Component} from "react";
import { Button } from "react-bootstrap";

class ViewProfileButton extends Component {

    handleClick(report) {
        var wnd = window.open("", "_blank");
        wnd.document.write(report)
    }

    render() {
        return (
            <Button className="view_profile_button" variant="btn btn-primary active btn-lg" onChange={() =>this.showButton(this.props.report_html)} onClick={() =>this.handleClick(this.props.report_html)}>Your Profile Report is Ready!</Button>
        )
    }
}

export default ViewProfileButton