import React from 'react';
import {useForm} from './useForm'
//import FirebaseAuthComponent from './firebase_config'
//import fireAuthUI from './firebase_config.js'



function SignUp () {
    const [values, handleChange]= useForm()
    return (
        <div>
        <p>Sign up is not available</p> 
        <p>In the future having account access will allow you to water the garden.</p>
        
        </div>
    )
}

export default SignUp