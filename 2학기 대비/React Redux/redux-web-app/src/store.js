import {createStore} from 'redux';

let initState = {
  // mode가 "WELCOME"이면, title: 'WEB', desc:'Hello, WEB'이 나올 것이고,
  // mode가 변경이 되면 해당 title, desc가 출력
  mode: 'WELCOME',
  welcome_content: {
    title: 'WEB',
    desc: 'Hello, WEB',
  },
  selected_content_id: 1,
  max_contents_id: 3, // 추가 생성되는 값에 +1해서 id를 부여함
  contents: [
    { id: 1, title: 'HTML', desc: 'HTML is ...'},
    { id: 2, title: 'CSS', desc: 'CSS is ...'},
    { id: 3, title: 'JavaScript', desc: 'JavaScript is ...'}
  ]
}

// state=initState 해준 부분 -> state가 없으면 initState를 넣어준다는 의미
function reducer(state=initState, action) {
  if (action.type === 'CHANGE_MODE'){
    return {...state, mode: 'WELCOME'};
  }
  if (action.type === 'READ') {
    return {...state, mode: 'READ', selected_content_id: action.id}
  }
  if (action.type === 'CREATE') {
    return {...state, mode: 'CREATE', selected_content_id: action.id}
  }
  if (action.type === 'CREATE_PROCESS') {
    let newId = state.max_content_id + 1
    let newContents = [
      ...state.contents
      ,{
        id: newId,
        title: action.title,
        desc: action.desc
      }
    ];
    return {
      ...state,
      contents: newContents,
      max_content_id: newId,
      mode: 'READ',
      selected_content_id: newId
    }
  }
  if (action.type === 'UPDATE') {
    return {...state, mode: 'UPDATE'}
  }
  return state;
}


// function reducer(state, action) {
//   if (state === undefined) {
//     return initState
//   }
// }

export default createStore(reducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ &&
  window.__REDUX_DEVTOOLS_EXTENSION__())