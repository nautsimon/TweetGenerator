import React from "react";
import "./Form.css";
import axios from "axios";
class Form extends React.Component {
  handleFormSubmit = event => {
    // event.preventDefault();
    const handle = event.target.elements.handle.value;
    event.preventDefault();
    return axios
      .post("http://127.0.0.1:8000/gen/", {
        handle: handle
      })
      .then(res => console.log(res))
      .catch(error => console.err(error));
  };
  render() {
    return (
      <form onSubmit={event => this.handleFormSubmit(event)} className="form'">
        <input name="handle" placeholder="Enter a Username" className="input" />
        <button className="button">Generate</button>
      </form>
    );
  }
}
export default Form;
