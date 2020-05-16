import React from 'react';
import {Link} from 'react-router-dom';
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
  <a className="button is-primary" href='/accounts/signup'>
                
              </a>
*/ 

function Header() {
    return (
      <div>
      <nav className="navbar is-primary" role="navigation" aria-label="main navigation">
      <div id="navbar" className="navbar-menu">
        <div className="navbar-start">
        <Link className="navbar-item is-size-4" to='/'>Home</Link>
        <Link className="navbar-item is-size-4" to='/about'>About</Link>
        <Link className="navbar-item is-size-4" to='/'>Live Data</Link>
        <Link className="navbar-item is-size-4" to='/water/waterGarden'>Water Garden</Link>
        </div>
        <div className="navbar-end">
          <div className="navbar-item">
            <div className="buttons">
            <Link className="button is-primary" to='/accounts/signup'><strong>Sign up</strong></Link>
            <Link className="button is-light" to='/accounts/login'><strong>Log in</strong></Link>
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