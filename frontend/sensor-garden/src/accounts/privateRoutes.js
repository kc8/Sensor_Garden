import React, { useContext } from "react";
//private route which will check for user context and if not null redirect to user desired page otherwise redirects to login screen
import { Route, Redirect } from "react-router-dom";
import { AuthContext } from "./authProvider";


const PrivateRoute = ({ component: RouteComponent, ...rest }) => {
  const {currentUser} = useContext(AuthContext);
  
  return (
    <Route
      {...rest}
      render={routeProps =>
        !!currentUser ? (<RouteComponent {...routeProps} />) : (<Redirect to={"/accounts/login"} />)
      }
    />
  );
};


export default PrivateRoute