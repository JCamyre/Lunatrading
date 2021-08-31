import logo from "./logo.svg";
import "./App.css";
import axios from "axios";
import React, { useEffect } from "react";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

function App() {
  const getStats = () => {
    // http://localhost:8000 don't need cause of the proxy value in package.json
    axios.get("/api/stats/").then((data) => {
      if (data) {
        console.log(data);
        return data;
      }
    });
  };

  useEffect(() => {
    getStats();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
