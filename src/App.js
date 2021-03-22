import './App.css';
import React, { useState, useEffect } from 'react';
import Button from '@material-ui/core/Button';
import axios from 'axios';
import { ResponsiveLine } from '@nivo/line'



function App() {
  //Determins if the program is started or stopped
  const [started, setStart] = useState(false);
  //Updating variable according to request results
  const [data, setData] = useState([]);

  //enables an interval to loop the request for the data form the DB
  useEffect(() => {
    if(started){
      const interval = setInterval(() => {
        ApiQuery();
      }, 1000);
   
      return () => clearInterval(interval);
    }
    
  }, [started]);

  //Using Nivo Graph using mostly default parameters
  const MyResponsiveLine = ({ data /* see data tab */ }) => (
    <ResponsiveLine
        data={data}
        lineWidth={0}
        isInteractive={false}
        margin={{ top: 50, right: 11, bottom: 50, left: 60 }}
        xScale={{ type: 'point' }}
        yScale={{ type: 'linear', min: 'auto', max: 'auto', stacked: true, reverse: false }}
        yFormat=" >-.2f"
        axisTop={null}
        axisRight={null}
        axisBottom={{
            orient: 'bottom',
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 75,
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
  //This function makes the flask server start the csv read->write process to the DB
  //May add a means of clearing the database on start to have a clean beginning
  function ApiCall() {
    axios.get('http://localhost:3000/start')
              .then(response => console.log(response) )
  }
  //This function queries the DB for all its current datapoints
  function ApiQuery() {     
        axios.get('http://localhost:3000/query')
      .then(response => setData(response.data.data) ) 
    }
    
  function ChangeState(value) {
    //Removes button to prevent more clicks
    setStart(value);
    //ApiCall is for starting the readings from the CSV ot be put into the database
    ApiCall();

    
    
  }
  

  return (
    <div className="App">
      <header className="App-header">
        <h1>
          BitCoin Grapher
        </h1>
        <p>By: Matthew MacMaster</p>
        {!started && 
        <Button variant="contained" color="primary" onClick={() => ChangeState(true) }>
          Start
        </Button> 
        }
        {started && 
        <Button variant="contained" color="primary" onClick={ () => ChangeState(false) }>
          Stop
        </Button> 
        } 
      </header>
        

      <div className="Graph">
        <MyResponsiveLine data= {data} />
      </div>
    </div>
  );
}

export default App;
