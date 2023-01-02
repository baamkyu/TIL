import React, {Component} from 'react'

export default class Create extends Component {
  render() {
    
    return (
      <form onSubmit={function(e) {
        e.preventDefault();
        this.props.onSubmit(
          e.target.title.value,
          e.target.desc.value
        );
      }.bind(this)}>
        <p>
          <input type="text" name="title"
          placeholder="제목을 입력하시오."></input>
        </p>
        <p>
          <textarea type="text" name="desc"
          placeholder="내용을 입력하시오."></textarea>
        </p>
        <p><input type="submit" value="생성"></input></p>
      </form>
    )
  }
}