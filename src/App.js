import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import Button from '@material-ui/core/Button';
import axios from 'axios';



function ApiCall2() {
  axios.get('http://localhost:3000/time')
            .then(response => console.log(response) )
}



function App() {
  const [started, setStart] = useState(true);
  const [data, setData] = useState([]);

  function ApiCall() {
    axios.get('http://localhost:3000/start')
              .then(response => console.log(response) )
  }
  function ApiQuery() {
    axios.get('http://localhost:3000/query')
              .then(response => console.log(response) )
  }
  function Start() {
    //ApiCall is for starting the readings from the CSV ot be put into the database
    ApiCall();
    //ApiQuery begins the process of querying the database for 
    ApiQuery();
    setStart(false);
  }
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          BitCoin Loader and Grapher
        </p>
        <br/>
        {started && 
        <Button variant="contained" color="primary" onClick={() => Start() }>
          Start
        </Button> 
        } 
        
        <Button variant="contained" color="primary" onClick={() => { ApiCall2() }}>
          Test
        </Button>
        <br/>

        <p>By: Matthew MacMaster</p>
      </header>
    </div>
  );
}

export default App;
