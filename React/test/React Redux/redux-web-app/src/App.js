import './App.css';
import Header from './components/Header'
import NavContainer from './containers/NavContainer'
import ReadContainer from './containers/ReadContainer'
import ControlContainer from './containers/ControlContainer'
import CreateContainer from './containers/CreateContainer';
import UpdateContainer from './containers/UpdateContainer';
import {connect} from 'react-redux'
import React, { Component } from 'react' 

class App extends Component {
  render() {
    let article = null;
    if (this.props.mode === "READ") {
      article = <ReadContainer></ReadContainer>
    } else if (this.props.mode === "CREATE") {
      article = <CreateContainer></CreateContainer>
    } else if (this.props.mode === "WELCOME") {
      article = <ReadContainer></ReadContainer>
    } else if (this.props.mode === "UPDATE") {
      article = <UpdateContainer></UpdateContainer>
    } 
    return (
      <div className="App">
        <Header></Header>
        <NavContainer></NavContainer>
        <ControlContainer></ControlContainer>
        { article }
      </div>
    );
  }
}

export default connect(
  function(state) {
    return {
      mode: state.mode
    }
  }
)(App);
