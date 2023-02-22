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

export default MeetupDetails;