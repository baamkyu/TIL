// domain.com/news/something-else
import { useRouter } from 'next/router'
function DetailPage() {
  const router = useRouter();
  const newsId = router.query.newsId
  // router.query.newsId로 얻은 값으로 백엔드 API에 요청보낼 수 있음
  // console.log(newsId)

  return <h1>DetailPage</h1> 
}
export default DetailPage;