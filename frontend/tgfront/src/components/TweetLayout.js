import React from "react";
import "./TweetLayout.css";

const TweetLayout = props => {
  return (
    <div className="tweet">
      <h1>{props.data}</h1>
    </div>
  );
};
export default TweetLayout;
