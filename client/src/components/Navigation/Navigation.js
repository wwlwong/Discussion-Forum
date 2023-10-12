import React from "react";
import { NavLink, useHistory } from "react-router-dom";
import { GiHamburgerMenu } from "react-icons/gi";

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


const Navigation = ({ updateUser }) => {
  const [menu, setMenu] = useState(false);

  const history = useHistory();

  const handleLogout = () => {
    console.log("handle logout");
    history.push("/");
  };

  const toggleMenu = () => setMenu((prev) => !prev);

  return (
    <div className="navigation">
      <h1 className="nav-title">Hot Deals</h1>
      <section className="nav-menu">
        {menu ? (
          <ul>
            <li className="close-button" onClick={() => setMenu(!menu)}>
              X
            </li>
            <li>
              <Link to="/"> Home</Link>
            </li>
            <li>
              <Link to="/post">All Deals</Link>
            </li>
            <li>
              <Link to="/post/new">New Post</Link>
            </li>
            <li>
              <Link to="/login"> Login</Link>
            </li>
            <li>
              <Link to="/signup"> Signup</Link>
            </li>
            <li className="logout-button" onClick={handleLogout}>
              {" "}
              Logout{" "}
            </li>
          </ul>
        ) : (
          <div className="hamburger-menu-wrapper" onClick={toggleMenu}>
            <GiHamburgerMenu size={30} />
          </div>
        )}
      </section>
    </div>
  );
};
export default Navigation;