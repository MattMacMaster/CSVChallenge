import './App.css';
import React, { useState } from 'react';
import Button from '@material-ui/core/Button';
import axios from 'axios';


function App() {
  const [started, setStart] = useState(true);
  const [data, setData] = useState([]);

  function ApiCall() {
    axios.get('http://localhost:3000/start')
              .then(response => console.log(response) )
  }
  function ApiQuery() {
    axios.get('http://localhost:3000/query')
              .then(response => setData(response.data) )
  }
  function Start() {
    //Removes button to prevent more clicks
    setStart(false);
    //ApiCall is for starting the readings from the CSV ot be put into the database
    ApiCall();
    //ApiQuery begins the process of querying the database for 
    //ApiQuery();
    
  }
  return (
    <div className="App">
      <header className="App-header">
        <p>
          BitCoin Loader and Grapher
        </p>
        <br/>
        {started && 
        <Button variant="contained" color="primary" onClick={() => Start() }>
          Start
        </Button> 
        } 
        
        <Button variant="contained" color="primary" onClick={() => { ApiQuery() }}>
          Update
        </Button>
        <br/>

        <p>By: Matthew MacMaster</p>
      </header>
    </div>
  );
}

export default App;
