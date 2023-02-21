import React, {Component} from 'react'
import {connect} from 'react-redux'

class Read extends Component {
  render() {
    return (
      <article>
        <h2>{this.props.title}</h2>
        {this.props.desc}
      </article>
    )
  }
}

export default connect()(Read);

/*
export default class Article extends Component {
  render() {
    return (
      <article>
        <h2>Welcome</h2>
        Hello, WEB.
      </article>
    )
  }
}
*/
