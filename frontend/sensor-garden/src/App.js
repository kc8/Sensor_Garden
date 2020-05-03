import React from 'react';
import { Route, Switch } from 'react-router-dom';
import SensorGroup from './services/sensorGroup.js' 
import Header from "./partials/header.js"
import Footer from "./partials/footer.js"
import About from "./About.js";
import SignUp from "./accounts/signup.js";

import './static/custom.css'; //custom css for a sticky footer. 


 function App() {
  
  return (
      <div className="Site"> 
        <Header />
        <main className="Site-content">
        <Switch>
          <Route path='/' component={SensorGroup} exact/>
          <Route path='/about' component={About} exact/>
          <Route path='/accounts/signup' component={SignUp} exact />
        </Switch> 
        </main> 
        <Footer />
      </div>
    );
}
export default App;
