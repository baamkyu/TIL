// domain.com/news
import { Fragment } from 'react'
import Link from 'next/Link'

function NewsPage() {
  return (
    <Fragment>
      <h1>The News Page</h1>
      <ul>
        <li>
          <Link href='news/nextjs-is-a-great-framework'>
            NextJS is a great framework
          </Link>
        </li>
        <li>
          <Link href='news/something-else'>
            Something Else
          </Link>
        </li>
      </ul>
    </Fragment>
  )
}
export default NewsPage;