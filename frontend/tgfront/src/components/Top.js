import React from "react";

class Top extends React.Component {
  state = { markov: "tweetGen1", tensor: "tweetGen2" };

  render() {
    return (
      <div className="genDiv row">
        <div className="bi centerH centerV">
          <Form />
        </div>
        <div className="bi centerH centerV">
          <div className="output">
            <TweetLayout data={this.state.markov} />
            <TweetLayout data={this.state.tensor} />
          </div>
        </div>
      </div>
    );
  }
}

export default Top;
