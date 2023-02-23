import MeetupList from '../components/meetups/MeetupList'
import { useState, useEffect } from 'react'
const DUMMY_MEETUPS = [
  {
    id: 'm1',
    title: 'first',
    image: 'https://upload.wikimedia.org/wikipedia/commons/f/f1/Action_off_toulon_4.jpg',
    address: 'first, 1234 City',
    description: 'first meetup'
  },
  {
    id: 'm2',
    title: 'second',
    image: 'https://upload.wikimedia.org/wikipedia/commons/f/f1/Action_off_toulon_4.jpg',
    address: 'second, 2345 City',
    description: 'second meetup'
  },
]
function HomePage(props) {
  return (
    <MeetupList meetups={props.meetups} />
  )
}
// export async function getServerSideProps(context) {
//   const req = context.req;
//   const res = context.res;
//   // fetch data from an API
//   return {
//     props: {
//       meetups: DUMMY_MEETUPS
//     }
//   }
// }

export async function getStaticProps() {
  // fetch data from an API
  return {
    props: {
      meetups: DUMMY_MEETUPS
    },
    revalidate: 1
  }
}

export default HomePage;