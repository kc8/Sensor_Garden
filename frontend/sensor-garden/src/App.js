import React from 'react';
import { Route, Switch } from 'react-router-dom';
import SensorGroup from './services/sensorGroup.js' 
import Clock from './clock.js'; 
import Header from "./partials/header.js"
import Footer from "./partials/footer.js"
import About from "./staticPages/about.js";

 function App() {
  
  return (
      <div className="App">
        <Header />
        <Switch>
          <Route path='/' component={SensorGroup} exact/>
          <Route path='/about' component={About} exact/>
        </Switch>      
      </div>
    );
}
export default App;
