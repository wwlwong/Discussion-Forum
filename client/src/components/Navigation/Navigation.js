import React from "react";
import { NavLink } from "react-router-dom";

const linkStyles = {
  display: "inline-block",
  
  width: "160px",
  padding: "12px",
  margin: "0 6px 6px",
  background: "#6900ff",
  textDecoration: "none",
  textAlign: "center",
  color: "white",
};

function NavBar() {
  return (
  <div className="navbar">
    <NavLink to="/" exact style={linkStyles} activeStyle={{background: "red",}}>Home</NavLink>
    <NavLink to='/post' style={linkStyles}
        activeStyle={{background: "red",}}>Hot Deals</NavLink>
    <NavLink to='/login' style={linkStyles}
        activeStyle={{background: "red",}}>Login</NavLink>
     <NavLink to='/signup' style={linkStyles}
        activeStyle={{background: "red",}}>Signup</NavLink>   
  </div>
  );
}

export default NavBar;