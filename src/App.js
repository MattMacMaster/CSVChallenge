import logo from './logo.svg';
import './App.css';
import React from 'react';
import Button from '@material-ui/core/Button';
import axios from 'axios';


function ApiCall() {
  axios.get('http://localhost:3000/time')
            .then(response => console.log(response) )
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          BitCoin Loader and Grapher
        </p>
        <br/>
        <Button variant="contained" color="primary" onClick={() => { ApiCall() }}>
          Start
        </Button>
        <br/>

        <p>By: Matthew MacMaster</p>
      </header>
    </div>
  );
}

export default App;
