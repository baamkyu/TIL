import './App.css';
import {useState} from 'react';

function Header(props) {
  return <header>
    <h1><a href="/" onClick={function(event) {
      event.preventDefault();
      props.onChangeMode();
    }}>{props.title}</a></h1>
  </header>
}
function Nav(props){
  const lis = []
  // topics의 원소의 수만큼 반복
  for (let i=0; i<props.topics.length; i++){
    let t = props.topics[i]
    lis.push(<li key={t.id}>
      <a id={t.id} href={'/read/'+t.id} onClick={event => {
      event.preventDefault();
      props.onChangeMode(Number(event.target.id));
    }}>{t.title}</a>
    </li>)
  }
  return <nav>
    <ol>
      {lis}
    </ol>
  </nav>
}
function Article(props) {
  return <article>
    <h2>{props.title}</h2>
    {props.body}
  </article>
}

function Create(props) {
  return <article>
    <h2>Create</h2>
    <form onSubmit={(event) => {
      event.preventDefault();
      const title = event.target.title.value
      const body = event.target.body.value
      props.onCreate(title, body);
    }}>
      <p><input type="text" name="title" placeholder="제목을 입력하시오."/></p>
      <p><textarea name="body" placeholder="내용을 입력하시오."></textarea></p>
      <p><input type="submit" value="CREATE"></input></p>
    </form>
  </article>
}



function App() {
  // const _mode = useState('WELCOME'); // WELCOME이라는 상태를 만듦
  // const mode = _mode[0]; // _mode의 값을 받음
  // const setMode = _mode[1]; // mode의 값을 바꿀 수 있음

  const [mode, setMode] = useState('WELCOME'); // 위 세줄과 같은 코드
  const [id, setId] = useState(null);
  const [nextId, setNextId] = useState(4);

  const [topics, setTopics] = useState([
    {id: 1, title: 'HTML', body: 'HTML is ...'},
    {id: 2, title: 'CSS', body: 'CSS is ...'},
    {id: 3, title: 'JavaScript', body: 'JavaScript is ...'},
  ])
  let content = null;

  if (mode === 'WELCOME') {
    content = <Article title="Welcome" body="Hello, WEB"></Article>
  } else if (mode === 'READ'){
    let title, body = null;
    for (let i=0; i<topics.length; i++) {
      if (topics[i].id === id) {
        title = topics[i].title;
        body = topics[i].body;
      }
    }
    content = <Article title={title} body={body}></Article>
  } else if (mode === 'CREATE') {
    content = <Create onCreate={(_title, _body) => {
      const newTopic = {id:nextId, title: _title, body: _body}
      const newTopics = [...topics]
      newTopics.push(newTopic);
      setTopics(newTopics);
      // 작성 후 상세페이지로 이동
      setMode('READ')
      setId(nextId)
      setNextId(nextId+1)
    }}></Create>
  }
  
  return (
    <div>
      <Header title="REACT" onChangeMode={function() {
        alert('Header');
        setMode("WELCOME");
      }}></Header>
      <Nav topics={topics} onChangeMode={(_id) => {
        alert(topics[_id-1].title); // 선택된 값이 alert창으로 뜨게 설정
        setMode("READ"); 
        setId(_id); // 누른 값의 id값을 담아서 해당하는 title, body값을 출력하는 데에 사용
      }}></Nav>
      {content}
      <a href="/create" onClick={(event) => {
        event.preventDefault();
        setMode('CREATE')
      }}>CREATE</a>
    </div>
  );
}

export default App;
 