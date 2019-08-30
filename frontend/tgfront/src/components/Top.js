import React from "react";
import "./Form.css";
import axios from "axios";
import titleImg from "../img/title.png";

import TweetLayout from "./TweetLayout";
import Scene from "./ThreeRenderAlt.js";
class Top extends React.Component {
  state = { markov: "enter username", username: "" };

  handleFormSubmit = event => {
    this.setState({ markov: "loading..." });
    // event.preventDefault();
    const handle = event.target.elements.handle.value;
    this.setState({ username: handle });
    event.preventDefault();
    return axios
      .post("http://127.0.0.1:8000/gen/", {
        title: handle
      })
      .then(response => {
        this.setState({ markov: response.data });
      })
      .catch(response => {
        this.setState({ markov: "not a valid username" });
      });
  };

  render() {
    return (
      <div className="genDiv">
        <div className="stretch">
          <Scene />
        </div>
        <img className="titleImg" src={titleImg} alt="titleImg" />
        <div className="row fullHeight">
          <div className="lCol bi centerH centerV">
            <form
              onSubmit={event => this.handleFormSubmit(event)}
              className="form'"
            >
              <label className="at">
                <b>@</b>
              </label>
              <input
                name="handle"
                placeholder="Enter a Username"
                className="input"
              />
              <button className="button">Generate</button>
            </form>
          </div>
          <div className="rCol bi centerH centerV">
            <TweetLayout
              data={this.state.markov}
              username={this.state.username}
            />
          </div>
        </div>
        <div className="bottomRow centerH">
          <a href="https://twitter.com/largeeggie">
            <p className="bottomText hover">[twitter]</p>
          </a>
          <a href="https://github.com/simonmahns">
            <p className="bottomText hover">[github]</p>
          </a>
          <a href="https://github.com/simonmahns/TweetGenerator">
            <p className="bottomText hover">[code]</p>
          </a>
          <a href="https://en.wikipedia.org/wiki/Markov_property">
            <p className="bottomText hover">[what is the markov property]</p>
          </a>
        </div>
      </div>
    );
  }
}

export default Top;
