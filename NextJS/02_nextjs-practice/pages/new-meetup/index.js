import NewMeetupForm from '../../components/meetups/NewMeetupForm'
function NewMeetUpPage() {
  function addMeetupHandler(enteredMeetupData) {
    console.log(enteredMeetupData)
  }
  return <NewMeetupForm onAddMeetup={ addMeetupHandler } />
}   

export default NewMeetUpPage;