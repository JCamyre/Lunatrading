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
        <img
          alt="T1"
          src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FC4pJkvsUMAA09-u.jpg%3Alarge&f=1&nofb=1"
        />
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
