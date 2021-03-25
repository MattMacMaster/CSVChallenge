import './App.css';
import React, { useState, useEffect } from 'react';
import Button from '@material-ui/core/Button';

import axios from 'axios';
import { ResponsiveLine } from '@nivo/line'



function App() {
  //A flag to determine if the program is started or stopped
  const [started, setStart] = useState(false);
  //Updating variable according to request results
  const [data, setData] = useState([]);
  // Sets a flag so that it doesnt run multiple instances of the data writer
  const [flag, setFlag] = useState(false);


  //enables an interval to loop the query data request 
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
        isInteractiv={false}
        margin={{ top: 50, right: 11, bottom: 80, left: 60 }}
        xScale={{ type: 'point' }}
        yScale={{ type: 'linear', min: 'auto', max: 'auto', stacked: true, reverse: false }}
        yFormat=" >-.2f"
        axisTop={null}
        colors={{ scheme: 'category10' }}
        axisRight={null}
        axisBottom={{
          orient: 'bottom',
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 85,
          legend: 'Date',
          legendOffset: 75,
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
        pointColor={{ from: 'color', modifiers: [] }}
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
  function Clear_DB() {     
      axios.get('http://localhost:3000/clear')
    .then(response => console.log(response) ) 
    setData([]);
  }
    
  function ChangeState(value) {
    //Removes button to prevent more clicks
    setStart(value);
    //ApiCall is for starting the readings from the CSV ot be put into the database
    if(!flag) {
      ApiCall();
      setFlag(true);
    }
  }

  return (
    <div className="App">
      <body>
        <ul>
          <li>
            <Button variant="contained" size="large"  color="primary"  onClick={ () => Clear_DB() }>
              Clear DB
            </Button> 
          </li>
          {!started && 
            <li>  
            <Button variant="contained" size="large" color="primary" onClick={() => ChangeState(true) }>
              Start
            </Button> 
          </li>
          }
          {started &&
          <li>
            <Button variant="contained" size="large" color="primary"  onClick={ () => ChangeState(false) }>
            Stop
            </Button> 
          </li>
          } 
          <li><a>By: Matthew MacMaster</a></li>

          <li><a>BitCoin Grapher</a></li>
        
          
        
        </ul>
      </body>
      

      <div className="Graph">
        <MyResponsiveLine data= {data} />
      </div>
    </div>
  );
}

export default App;
