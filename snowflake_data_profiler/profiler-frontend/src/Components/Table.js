import React, {Component} from 'react';
import { Button, Form, Spinner} from "react-bootstrap";


class ProfilerForm extends Component {
  

  constructor(props) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.state = {
      validated: false,
      isLoading: false,
      error: null,
    };
  }

  handleSubmit = (event) => {
    const form = event.currentTarget;
    if (form.checkValidity() === false) {
      event.preventDefault();
      event.stopPropagation();
    }

    event.preventDefault();
    this.setState({isLoading:true});
    const data = new FormData(event.target);
    this.setState({validated:true, error: null});
    fetch('/report', {
      method:"POST",
      body: data,
      headers:{
        "content_type":"multpart/form-data",
      },
  
    })
    .then(r => {return r.json()})
    .then(r => {
      if (r.status === 'ok') {
        var wnd = window.open("", "_blank");
        wnd.document.write(r.profile_report);
        this.setState({isLoading:false});
        return r;
      } else {
        this.setState({error: r.error, isLoading: false});
        return r;
      }
    })
    .then(r => {console.log(r)})
  }

  render() {
    let {error, isLoading} = this.state;

    const renderError = ()=>{
      if(error) {
        return <p className="error">{error}</p>
      } else {
        return
      }
    }

    const renderSpinning = ()=>{
      if(isLoading) {
        return <Spinner className='spinner' animation="border" variant="primary" size={150}><span className="sr-only">Loading...</span></Spinner>
      } else {
        return
      }
    }

    return (
      <div className="container">
      <div className="py-5 text-center">
          <h2>Generate a data profile of the first 10K rows of one of your Snowflake tables</h2>
          {renderError()}
          {renderSpinning()}
      </div>
      <div class="row">
      <div class="col-8 col-xs-12 order-md-1 mx-auto">
        <h4 class="mb-3">Snowflake details:</h4>
    <div className='full_page'>
          <Form id='profiler-form' className="needs-validation" noValidate validated={this.state.validated} onSubmit={this.handleSubmit}>
              <Form.Group md="4" controlId="username">
                <Form.Label>Snowflake Username</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="elon.musk@tesla.com"
                  name="username"
                />
                <Form.Control.Feedback type="invalid">Please enter your Snowflake username.</Form.Control.Feedback>
              </Form.Group>
              <Form.Group md="4" controlId="password">
                <Form.Label>Snowflake Password</Form.Label>
                <Form.Control
                  required
                  type="password"
                  placeholder="cybertruck2021"
                  name="password"
                />
                <Form.Control.Feedback type="invalid">Please enter your Snowflake password.</Form.Control.Feedback>
              </Form.Group>
              <Form.Group md="4" controlId="url">
                <Form.Label>Snowflake URL<span className="text-muted"> (or account name)</span></Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="https://tesla.snowflakecomputing.com"
                  name="url"
                />
                <Form.Control.Feedback type="invalid">Please enter your Snowflake URL.</Form.Control.Feedback>
              </Form.Group>
              <Form.Group md="4" controlId="role">
                <Form.Label>Snowflake Role<span className="text-muted"> (Optional)</span></Form.Label>
                <Form.Control
                  type="text"
                  placeholder="CEO"
                  name="role"
                />
              </Form.Group>
              <Form.Group md="4" controlId="warehouse">
                <Form.Label>Snowflake Warehouse<span className="text-muted"> (Optional)</span></Form.Label>
                <Form.Control
                  type="text"
                  placeholder="FLAMETHROWER_REPORTING_WH"
                  name="warehouse"
                />
              </Form.Group>
              <Form.Group md="4" controlId="database">
                <Form.Label>Snowflake Database</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="PRODUCTION"
                  name="database"
                />
                <Form.Control.Feedback type="invalid">Please enter your Snowflake database name.</Form.Control.Feedback>
              </Form.Group>
              <Form.Group md="4" controlId="schema">
                <Form.Label>Snowflake Schema</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="INVENTORY"
                  name="schema"
                />
                <Form.Control.Feedback type="invalid">Please enter your Snowflake schema name.</Form.Control.Feedback>
              </Form.Group>
              <Form.Group md="4" controlId="table">
                <Form.Label>Snowflake Table or View</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="MODEL_Y_INVENTORY"
                  name="table"
                />
                <Form.Control.Feedback type="invalid">Please enter your Snowflake table or view name.</Form.Control.Feedback>
              </Form.Group>
            <Button variant="btn btn-primary btn-lg btn-block" type="submit" id="submit_button">Create data profile</Button>
          </Form>
        </div>
      </div>
    </div>
    </div>
    )
  }
}


export default ProfilerForm