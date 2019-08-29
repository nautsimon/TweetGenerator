import React from "react";
import Top from "./components/Top";
import Bottom from "./components/Bottom";
import "./App.css";
import "antd/dist/antd.css";
function App() {
  return (
    <div className="App">
      <Top />
      <Bottom />

      <div className="row centerH">
        <p>[Created by Simon Mahns] </p>
        <p> </p>
        <p> [twitter] </p>
        <p> </p>
        <p> [code for this site] </p>
        <p> </p>
        <p> [github]</p>
      </div>
    </div>
  );
}

export default App;
