import React, {Component} from 'react'
import {connect} from 'react-redux'

class Header extends Component {
  render() {
    return (
      <header>
        <h1><a href="#" onClick={function() {
          this.props.onClick();
        }.bind(this)}>WEB</a></h1>
        World Wide WEB
      </header>
    )
  }
}

export default connect(
  null,
  function(dispatch){
    return {
      onClick: function() {
        // 클릭이벤트가 발생하면 CHANGE_MODE 액션을 취하고 해당 액션으로 인해 mode는 WELCOME으로 바뀜
        dispatch({type: 'CHANGE_MODE', mode: 'WELCOME'})
      }
    }
  })(Header);

/*
export default class Header extends Component {
  render() {
    return (
      <header>
        <h1>WEB</h1>
        World Wide Web
      </header>
    )
  }
}
*/