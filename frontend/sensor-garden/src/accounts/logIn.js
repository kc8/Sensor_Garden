import React, { Component, useState, useContext } from 'react';
import { useForm } from './useForm'
import {fireAuth} from "./firebase_config.js"
import { AuthContext } from "./authProvider";

function LogIn() {
    const [values, handleChange]= useForm({email: "", password: ""})

    function validate() { 
        return this.state.email.length > 0 && this.state.password.length > 0; 
    }

    function handleSubmit(event) {
        console.log()
        event.preventDefault(); //prevents reload of webpage
        const loginPromise = fireAuth.signInWithEmailAndPassword(values.email, values.password); 
        loginPromise.catch(e => console.log(e.message));
        fireAuth.onAuthStateChanged(firebaseUser => { 
            if(firebaseUser) { 
                console.log(firebaseUser)
            } else {
                console.log("Not Logged in");
            }
        })
    }
    
    return (
        <div>
            <form onSubmit={handleSubmit}>
            <label>
                Email:
                <input type="text" name="email" value={values.email} onChange={handleChange}/>
            </label>
            <label>
                Password:
                <input type="password" name="password" value={values.password} onChange={handleChange}/>
            </label>
                <input type ="submit" value="Submit" />
            </form>
        </div>
    );  

}

export default LogIn;


