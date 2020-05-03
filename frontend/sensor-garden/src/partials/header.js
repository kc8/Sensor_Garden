import React from 'react';
//import {Link} from 'react-router-dom';
import Clock from '../clock.js'; 

/*
Adds in the header and Nav bar at the of the window

Future Responsive menu: 
<nav className="main">
        <ul>
          <li className="menu">
            <a className="fas fa-bars" href="#menu" >Menu</a>
          </li>
        </ul>
      </nav>
  <li><Link to='/'>Home</Link></li>
*/ 
function Header() {
    return (
      <div>
      <nav class="navbar is-primary" role="navigation" aria-label="main navigation">
        <div className="navbar-brand">
          <a className="navbar-item" href="">
            <img src="" width="112" height="28"></img>
          </a>
        </div>
      <div id="navbar" className="navbar-menu">
        <div className="navbar-start">
          <a className="navbar-item is-size-4" href='/'>
            Home
          </a>
              <a className="navbar-item is-size-4" href='/about'>
                About
              </a>
        </div>

        <div className="navbar-end">
          <div className="navbar-item">
            <div className="buttons">
              <a className="button is-primary">
                <strong>Sign up</strong>
              </a>
              <a className="button is-light">
                Log in
              </a>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <section className="hero is-primary">
    <div className="hero-body">
      <div className="container">
        <h1 className="title">Sensor Garden</h1>
        <h2 className="subtitle">  
          <Clock></Clock>
        </h2>
      </div>   
    </div>
</section>
    </div>
      ) 
  }

  export default Header;