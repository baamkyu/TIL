import React, {Component} from 'react';
import './App.css';
import AddNumberRoot from './components/AddNumberRoot.jsx'
import DisplayNumberRoot from './components/DisplayNumberRoot.jsx'


class App extends Component {cd
  state = {number: 0}
  render(){
    return (
      <div className="App">
        <h1>Root</h1>
        <AddNumberRoot></AddNumberRoot>
        <DisplayNumberRoot></DisplayNumberRoot>
      </div>
    );
  }
}

export default App;
