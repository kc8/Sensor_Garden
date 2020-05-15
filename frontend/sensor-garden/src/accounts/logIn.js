//Display login form if not logged in or logout/ basic user inforamtion. Upon login will log the user in and set it to context. 
import React, { useContext, useCallback } from 'react';
import { useForm } from './useForm'
import {fireAuth} from "./firebase_config.js"
import {withRouter, Redirect} from "react-router";
import { AuthContext } from "./authProvider";


const LogIn = ({history}) => {     
    const [values, handleChange]= useForm({email: "", password: ""});

    const handleSubmit = useCallback(
        async event => { 
            event.preventDefault(); 
            const {email, password} = event.target.elements; 
            try {
                await fireAuth.signInWithEmailAndPassword(email.value, password.value);
                 history.push("/water/waterGarden");
            } catch(error) {
                console.log(error);
            }
        }, 
        [history]
    );
    
    const {currentUser} = useContext(AuthContext);

    //To-Do: Instead return a log out button and a 'profile' page? 
    if (currentUser) { 
        //return <div>You are already logged in!</div>
    }
    
    return (
        <div className="field">
            <div class="hero-body">
                <div class="container">
                    <div class="columns is-centered">
                        <div class="column is-5-tablet is-4-desktop is-3-widescreen">
                            <label className="label is-medium">Login</label>
                            <div class="control">
                                <form className="box" onSubmit={handleSubmit}>
                                <label className="label">
                                    Email:
                                    <input className="input" placeholder="Email" type="text" name="email" value={values.email} onChange={handleChange}/>
                                </label>
                                <label className="label">
                                    Password:
                                    <input className="input" placeholder="Password" type="password" name="password" value={values.password} onChange={handleChange}/>
                                </label>
                                <div className="field is-grouped">
                                    <div className="control">
                                        <button className="button is-link is-light" type="submit" value="Submit">Login</button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div> 
            </div>
        </div>
    );  

}

export default withRouter(LogIn);