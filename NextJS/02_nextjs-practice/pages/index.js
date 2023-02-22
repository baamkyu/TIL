import MeetupList from '../components/meetups/MeetupList'
import { useState, useEffect } from 'react'
const DUMMY_MEETUPS = [
  {
    id: '1',
    title: 'first',
    image: 'https://upload.wikimedia.org/wikipedia/commons/f/f1/Action_off_toulon_4.jpg',
    address: 'first, 1234 City',
    description: 'first meetup'
  },  
  {
    id: '2',
    title: 'second',
    image: 'https://upload.wikimedia.org/wikipedia/commons/f/f1/Action_off_toulon_4.jpg',
    address: 'second, 2345 City',
    description: 'second meetup'
  },
]
function HomePage() {
  const [ loadedMeetups, setLoadedMeetups ] = useState([])
  useEffect(() => {
    setLoadedMeetups(DUMMY_MEETUPS)
  }, [])
  return (
  <MeetupList meetups={DUMMY_MEETUPS} />
  )
}   
export default HomePage;