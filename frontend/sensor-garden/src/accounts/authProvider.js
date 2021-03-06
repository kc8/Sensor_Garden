import React, {useEffect, useState, createContext} from 'react'; 
import {fireAuth} from './firebase_config.js'

export const AuthContext = createContext(null);

//Provides the login information to all componenets that are wrapped with this. 
export const AuthProvider = ({children}) => { 
    const [currentUser, setCurrentUser] = useState(null); 

    useEffect(() => {
        fireAuth.onAuthStateChanged(setCurrentUser); 
    }, []);

    return (
        <AuthContext.Provider value={{currentUser}} > 
            {children}
        </AuthContext.Provider>
    );
};