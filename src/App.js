import './App.css';
import React, { useState, useEffect } from 'react';
import Button from '@material-ui/core/Button';
import axios from 'axios';
import { ResponsiveLine } from '@nivo/line'



function App() {
  const [started, setStart] = useState(true);
  const [data, setData] = useState([]);

  
  const MyResponsiveLine = ({ data /* see data tab */ }) => (
    <ResponsiveLine
        data={data}
        margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
        xScale={{ type: 'point' }}
        yScale={{ type: 'linear', min: 'auto', max: 'auto', stacked: true, reverse: false }}
        yFormat=" >-.2f"
        axisTop={null}
        axisRight={null}
        axisBottom={{
            orient: 'bottom',
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 90,
            legend: 'Date',
            legendOffset: 36,
            legendPosition: 'middle'
        }}
        axisLeft={{
            orient: 'left',
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: 'Price',
            legendOffset: -40,
            legendPosition: 'middle'
        }}
        pointSize={10}
        pointColor={{ theme: 'background' }}
        pointBorderWidth={2}
        pointBorderColor={{ from: 'serieColor' }}
        pointLabelYOffset={-12}
        useMesh={true}
        
    />
)


function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}


  function ApiCall() {
    axios.get('http://localhost:3000/start')
              .then(response => console.log(response) )
  }
  async function ApiQuery() {
    while (true) {

      axios.get('http://localhost:3000/query')
      .then(response => setData(response.data.data) )      
      await sleep(3000);

    }
    
  }
  function Start() {
    //Removes button to prevent more clicks
    setStart(false);
    //ApiCall is for starting the readings from the CSV ot be put into the database
    ApiCall();
    //ApiQuery begins the process of querying the database for 
    ApiQuery();
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>
          BitCoin Grapher
        </h1>
      </header>
      <div className="Graph">
        <MyResponsiveLine data= {data} />
      </div>

      {started && 
        <Button variant="contained" color="primary" onClick={() => Start() }>
          Start
        </Button> 
        } 
        
        <br/>
        
        <br/>
        <Button variant="contained" color="primary" onClick={() => { Start() }}>
          Update
        </Button>

      <p>By: Matthew MacMaster</p>
    </div>
  );
}

export default App;
