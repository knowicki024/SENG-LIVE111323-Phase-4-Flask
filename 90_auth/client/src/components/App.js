import { useEffect, useState } from "react"
import Home from "./Home"
import Signup from "./Signup"
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

function App() {

  const [user, setUser] = useState(null)

  useEffect(() => {
    fetchUser()
  },[])

  const fetchUser = () => (
    fetch('/signup')
    .then(res => {
      if(res.ok){
        res.json()
        .then(data => {
          setUser(data)
          fetchProductions()
        })
      } else {
        console.log('hi')
        setUser(null)
      }
    })
  )

  return (
    <div className="App">
      <Router>
        <Switch>
            <Route 
              path="/signup" 
              component={Signup}
              updateuser={ updateUser }/>

            <Route 
              path="/" 
              component={Home} />
         </Switch>
      </Router>
    </div>
  );
}

export default App;
