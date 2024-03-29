import Update from '../components/Update'
import { connect } from 'react-redux'
export default connect(
  function(state) {
    let title, desc, id;
    for (let i=0; i<state.contents.length; i++){
      let d = state.contents[i]
      if (d.id === state.selected_content_id) {
        title = d.title;
        desc = d.desc;
        id = d.id;
        break;
      }
    }
    return {
      title: title,
      desc: desc,
      id
    }
  },
  function(dispatch) {
    return {
      onSubmit: function(id, title, desc) {
        dispatch({type: 'UPDATE_PROCESS', id: id, title: title, desc: desc})
      }
    }
  }
) (Update)