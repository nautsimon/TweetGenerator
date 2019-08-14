import React from "react";
import Top from "./components/Top";
import { BrowserRouter as Router } from "react-router-dom";
import BaseRouter from "./routes";

import "antd/dist/antd.css";
function App() {
  return (
    <div className="App">
      <Top />
    </div>
  );
}

export default App;
