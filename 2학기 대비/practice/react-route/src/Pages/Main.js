import React from 'react'
import { Link } from 'react-router-dom'

function Main() {
  return (
    <div>
      <h1>메인 페이지이지만, 상품 페이지로 갈 수 있는 리스트들을 아래 ul태그로 보여줄 것임</h1>
      <ul>
        <Link to='product/1'><li>1번 상품</li></Link>
        <Link to='product/2'><li>2번 상품</li></Link>
      </ul>
    </div>
  )
}

export default Main