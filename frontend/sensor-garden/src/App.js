import React, {Component, useState, useEffect} from 'react';
import UpdateSensorData from './services/SensorData.js';
import {ApolloClient, ApolloLink} from 'apollo-boost';
import { ApolloProvider } from '@apollo/react-hooks';
import { InMemoryCache } from "apollo-cache-inmemory";
import { HttpLink } from "apollo-link-http";
import logo from './logo.svg';
import Clock from './clock.js'; 

import './App.css';

const cache = new InMemoryCache();

const link = new HttpLink({
  uri: "https://tomato-sensor.ue.r.appspot.com/"
});

const client = new ApolloClient({
  link,
  cache
});

 function App() {
  
  return (
      <div className="App">
      <ApolloProvider client={client}>
      <UpdateSensorData></UpdateSensorData>
      <Clock></Clock>
      </ApolloProvider>
      </div>
    );
}

export default App;