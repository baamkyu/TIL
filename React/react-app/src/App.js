import './App.css';
import {useState} from 'react';

function Header(props) {
  return <header>
    <h1><a href="/" onClick={function(event) {
      event.preventDefault(); // a태그의 하이퍼링크 기능을 막아주는 기능
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

function Update(props) {
  const [title, setTitle] = useState(props.title);
  const [body, setBody] = useState(props.body);

  return <article>
    <h2>Update</h2>
    <form onSubmit={(event) => {
      event.preventDefault();
      const title = event.target.title.value
      const body = event.target.body.value
      props.onUpdate(title, body);
    }}>
      <p><input type="text" name="title" placeholder="제목을 수정하시오." value={title} onChange={event=>{
        setTitle(event.target.value);
      }}/></p>
      <p><textarea name="body" placeholder="내용을 수정하시오." value={body} onChange={event=>{
        setBody(event.target.value);
      }}></textarea></p>
      <p><input type="submit" value="Update"></input></p>
    </form>
  </article>
}


function App() {
  // const _mode = useState('WELCOME'); // WELCOME이라는 상태를 만듦
  // const mode = _mode[0]; // 'WELCOME' (상태의 값을 읽을 때 사용)
  // const setMode = _mode[1]; // 0번째 원소(상태)의 값을 변경할 때 사용하는 함수

  const [mode, setMode] = useState('WELCOME'); // 위 세줄과 같은 코드
  const [id, setId] = useState(null);
  const [nextId, setNextId] = useState(4);

  const [topics, setTopics] = useState([
    {id: 1, title: 'HTML', body: 'HTML is ...'},
    {id: 2, title: 'CSS', body: 'CSS is ...'},
    {id: 3, title: 'JavaScript', body: 'JavaScript is ...'},
  ])
  let content = null;
  let contextControl = null; // UPDATE를 할 수 있는 곳인지 확인

  if (mode === 'WELCOME') {
    content = <Article title="Welcome" body="Hello, WEB"></Article>
  } else if (mode === 'READ'){
    // detail 페이지로 이동하려고 할 때, 선택한 곳의 페이지로 이동
    let title, body = null;
    for (let i=0; i<topics.length; i++) {
      if (topics[i].id === id) {
        title = topics[i].title;
        body = topics[i].body;
      }
    }
    content = <Article title={title} body={body}></Article>
    // detail 페이지에 있을 때만 update할 수 있는 로직 추가
    contextControl = <>
      <li><a href={'/update'+id} onClick={event => {
        event.preventDefault();
        setMode('UPDATE');
        }}>UPDATE</a></li>
      <li><input type="button" value="DELETE" onClick={() => {
		// detail 페이지에 있을 때만 delete할 수 있는 로직 추가
        const newTopics = []
        // newTopics라는 새로운 리스트를 생성하고
        // 삭제하려는 항목을 delete하면 그 항목을 제외한 나머지 항목들을
        // newTopics에 push해주면 삭제한 것 처럼 작동한다.
        for (let i=0; i<topics.length; i++) {
          if (topics[i].id !== id) {
            newTopics.push(topics[i]);
          }
        }
        setTopics(newTopics);
        setMode('WELCOME')
      }}/></li>
    </>
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
  } else if (mode === 'UPDATE') {
    let title, body = null;
    for (let i=0; i<topics.length; i++){
      if (topics[i].id === id){
        title = topics[i].title;
        body = topics[i].body;
      }
    }
    content = <Update title={title} body={body} onUpdate={(title, body) => {
      const newTopics = [...topics]
      const updatedTopic = {id: id, title: title, body: body}
      for (let i=0; i<newTopics.length; i++){
        if (newTopics[i].id === id) {
          newTopics[i] = updatedTopic;
          break;
        }
      }
      setTopics(newTopics);
      setMode('READ');

  }}></Update>
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
      <ul>
        <li> 
          <a href="/create" onClick={(event) => {
          event.preventDefault();
          setMode('CREATE')
          }}>CREATE</a>
        </li>
        {contextControl}
      </ul>
    </div>
  );
}

export default App;
 