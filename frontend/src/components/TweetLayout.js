import React from "react";
import "./TweetLayout.css";
import profImg from "../img/prof.png";
import bottomBorder from "../img/bar.PNG";

const TweetLayout = props => {
  return (
    <div className="twtDiv">
      <div className="twtRow">
        <div className="twtImgDiv">
          <img src={profImg} className="profImg" alt="profImg"></img>
        </div>
        <div className="twtMainDiv">
          <div className="twtRow">
            <p className="black twtPad">
              <b>tweetgen.xyz</b>
            </p>

            <p className="">@{props.username}</p>

            <p className="twtPadBi"> · </p>

            <p className="">1 min</p>
          </div>
          <p className="black twtMainText">{props.data}</p>
          <img src={bottomBorder} alt="bottom" className="borderImg" />
        </div>
      </div>
    </div>
  );
};
export default TweetLayout;
