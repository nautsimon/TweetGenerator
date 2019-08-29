import React from "react";
import Form from "./Form";
import titleImg from "../img/titleImg.png";
import TweetLayout from "./TweetLayout";
class Top extends React.Component {
  state = { markov: "tweetGen1", tensor: "tweetGen2" };

  render() {
    return (
      <div className="genDiv">
        <img className="titleImg" src={titleImg} alt="titleImg" />
        <div className="row fullHeight">
          <div className="bi centerH centerV">
            <div>
              <Form />
            </div>
          </div>
          <div className="bi centerH centerV">
            <div className="output">
              <TweetLayout data={this.state.markov} />
              <TweetLayout data={this.state.tensor} />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Top;
