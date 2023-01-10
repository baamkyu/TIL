import './App.css';
import Header from './Pages/Header'
import Main from './Pages/Main'
import Product from './Pages/Product'
import NotFound from './Pages/NotFound'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path='/' element={<Main/>}></Route>
          <Route path='/product/:productId' element={<Product/>}></Route>
          {/* 상단에 위치하는 라우트들의 규칙을 모두 확인 후, 일치하는 라웉가 없는 경우 NotFound로 보냄 */}
          <Route path='*' element={<NotFound/>}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
