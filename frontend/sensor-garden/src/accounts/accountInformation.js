import React, {useEffect, useState, useContext} from 'react'; 
import {fireAuth} from './firebase_config.js'
import { AuthContext } from "./authProvider";



function AccountInformationDisplay() { 
    const {currentUser} = useContext(AuthContext);
    console.log("Current user value:", currentUser)
    return (
        <div>
        Name:
        </div>
    )
}

export default AccountInformationDisplay;