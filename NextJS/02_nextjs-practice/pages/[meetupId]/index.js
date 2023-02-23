import { Fragment } from "react";
import MeetupDetail from '../../components/meetups/MeetupDetail'
function MeetupDetails() {
  return (
    <MeetupDetail
      image='https://upload.wikimedia.org/wikipedia/commons/f/f1/Action_off_toulon_4.jpg'
      title='A First Meetup'
      address="Some Street 5, Some City"
      description="The meetup description"
    />
  )
}

// 미트 업 데이터는 아주 자주 바뀌지 않음. 추가하는 기능만 있음 -> getStaticProps
export async function getStaticPaths() {
  return {
    // 특정 path를 정의함 (모든 path가 아니라)
    fallback: false,
    paths: [
      // 하드코드 했지만 현실 코드에서는 API사용해서
      {
        params: {
          meetupId: 'm1'
        }
      },
      {
        params: {
          meetupId: 'm2'
        }
      }
    ]
  }
}
export async function getStaticProps(context) {

  const meetupId = context.params.meetupId

  return {
    props: {
      meetupData: {
        image: 'https://upload.wikimedia.org/wikipedia/commons/f/f1/Action_off_toulon_4.jpg',
        id: meetupId,
        title: 'A First Meetup',
        address: "Some Street 5, Some City",
        description: "The meetup description",
      }
    }
  }
}
export default MeetupDetails;