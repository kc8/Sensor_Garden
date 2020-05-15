import React from 'react';
import { Route, Switch } from 'react-router-dom';
import SensorGroup from './services/sensorGroup.js' 
import Header from "./partials/header.js"
import Footer from "./partials/footer.js"
import About from "./About.js";
import SignUp from "./accounts/signup.js";
import LogIn from "./accounts/logIn.js"
import { AuthProvider } from "./accounts/authProvider.js";
import WaterGarden from "./services/waterGarden/waterGarden.js"
import PrivateRoute from "./accounts/privateRoutes.js";
import AccountInformationDisplay from './accounts/accountInformation.js'

import './static/custom.css'; //custom css for a sticky footer. 

 function App() {
  
  return (
    <AuthProvider>
      <div className="Site"> 
        <Header />
        <main className="Site-content">
        <Switch>
          <Route path='/' component={SensorGroup} exact/>
          <Route path='/about' component={About} exact/>
          <Route path='/accounts/signup' component={SignUp} exact />
          <Route path='/accounts/login' component={LogIn} exact />
          <PrivateRoute path='/water/waterGarden' component={WaterGarden} exact />
        </Switch> 
        </main> 
        <Footer />
      </div>
      </AuthProvider>
    );
}
export default App;
