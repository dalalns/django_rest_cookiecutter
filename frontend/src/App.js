import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

class App extends Component {
  render() {
    return (
    <div>
    <button type="button" onClick={this.onClick}>Send GET /studentss</button>
    </div>
    );
}

onClick(ev) {
    console.log("Sending a GET API Call !!!");
    axios.get('http://localhost:8000/api/students')
    .then((response) => {
    console.log(response.data);
    console.log(response.status);
    console.log(response.statusText);
    console.log(response.headers);
    console.log(response.config);
  });
}

}

export default App;
