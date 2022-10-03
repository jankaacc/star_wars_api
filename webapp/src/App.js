import React, { useState, useEffect } from 'react';
import axios from 'axios';

import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

const API_URL = 'http://localhost:5000/backend/api/people'

const paths = {
  home: '/',
  detail: '/:id'
}

function App() {
  return (
    <div>
      <Router>
        <Switch>
          <Route exact path={paths.detail} component={Detail} />
          <Route exact path={paths.home} component={Home} />
        </Switch>  
      </Router>
    </div>
  );
}

function Detail(props) {
  const currentSite = `${API_URL}${props.location.pathname}`;

  const groupByOptions = [
    "date",
    "gender",
    "birth_year",
    "eye_color",
    "hair_color",
    "height",
    "homeworld",
    "mass",
    "name",
    "skin_color",
  ]

  const [data, setData] = useState([]);
  const [results, setResults] = useState([]);
  const [countBy, setCountBy] = useState([]);
  const [columns, setColumns] = useState(groupByOptions);
  const [loading, setLoading] = useState(false);
 
  const fetchData = async (url) => {
    const response = await axios(url);
    setData(response.data);
    setResults([...results, ...response.data.results]);
  };

  const groupData = async (column) => {
    setLoading(true);
    const unique = [...new Set([...countBy, column])];
    setCountBy(unique);
    setColumns([...unique, "value"]);
    
    const response = await axios(`${currentSite}?count_by=${unique.join()}`);
    setData(response.data);
    setResults(response.data.results);
    setLoading(false);
  };

  useEffect(() => {
    fetchData(currentSite);
  }, []);

  const renderHead = () => {
    if(!loading){
    return (
      <thead>
          <tr>
          {columns.map((headerCell, index) => (
            <th key={`header${index}`}>
              {headerCell}
            </th>
          ))}
          </tr>
        </thead>
    )
          }
  }

  const renderBody = () => {
    if (results && !loading){
      return (<tbody >
        {results.map((rowData, index) => (
        <tr key={`outer${index}`}>
          {columns.map((cell, index) => (
          <td key={`iner${index}`}>
            { rowData[cell] }
          </td>
          ))}
        </tr>
        ))}
      </tbody>)
    } else {
      return <tbody></tbody>
    }
  }

  return (
    <div>
      {groupByOptions.map((headerCell) => (
          <button onClick={() => {groupData(headerCell)}}>
            {headerCell}
          </button>
      ))}
      <table>
        {renderHead()}
        {renderBody()}
      </table>
      <button
        type="button"
        onClick={() => fetchData(data.next)}
      >
        Load More
      </button>
    </div>
  );
}

function Home() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios(
        API_URL,
      );

      setData(response.data);
    };

    fetchData();
  }, []);

  return (
    <div>
      <button
        type="button"
        onClick={() => axios(`${API_URL}/download`)}
      >
        Download
      </button>
      <ul>
        {data.map(item => {
          const detailPath = `/${item.id}`
          return (<li key={item.id}>
            <a href={detailPath}>{item.filename}</a>
          </li>)
        })}
      </ul>
    </div>
  );
}

export default App;