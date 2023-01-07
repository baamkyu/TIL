import './App.css';
import { Link, Route, Routes } from 'react-router-dom'
import { Hello } from './pages/Hello.js'
import { Bye } from './pages/Bye.js'

function App() {
  return (
    <>
      <nav>
        <li>
          <Link to='/'>Hello</Link>
        </li>
        <li>
          <Link to='/bye'>Bye</Link>
        </li>
      </nav>
      <Routes>
        <Route path="/" element={<Hello/>}></Route>
        <Route path="/bye" element={<Bye/>}></Route>
      </Routes>
    </> 
    );  
}

export default App;
