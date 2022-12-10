import React, {Component} from 'react';
import AddNumber from '../components/AddNumber.jsx'

export default class AddNumberRoot extends Component{
  render() {
    return (
      <div>
        <h1>Add Number Root</h1>
        <AddNumber></AddNumber>
      </div>
    )
  }
}