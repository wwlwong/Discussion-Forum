import { useState, useEffect } from "react";
import { Route, Routes } from "react-router-dom";
import Navigation from "./components/Navigation/Navigation";
import Home from "./components/Home/Home";
import "./App.css";
import Authentication from "./components/Authentication/Authentication";
import NewPostForm from "./components/NewPostForm/NewPostForm";
import PostDetail from "./components/PostDetail/PostDetail";

function App() {
  const [post, setPost] = useState([]);
  const [user, setUser] = useState(null);

  useEffect(() => {
    // fetchUser()
    // fetchProductions()
  }, []);

  const fetchPost = () => {
    fetch("/post")
      .then((res) => res.json())
      .then(setPost);
  };

  const fetchUser = () => {
    /*
    Create a GET fetch that goes to '/authorized'
      - If returned successfully set the user to state and fetch our productions
      - else set the user in state to Null
    */
  };

  const addPost = (post) =>
    setPost((current) => [...current, post]);

  const updateUser = (user) => setUser(user);

  /*
    Restrict access to app
      - If the user is not in state, return JSX and include <Navigation/> and <Authentication updateUser={updateUser}/>
      - Test out our route! Logout and try to visit other pages. Login and try to visit other pages again. Refresh the page and note that you are still logged in! 
  */

  return (
    <>
      <Navigation updateUser={updateUser}/>
      <Routes>
        <Route
          path={"/post/new"}
          element={
            <div>
              <NewPostForm addPost={addPost} />
            </div>
          }
        />
        <Route path={"/post/:id"} element={<PostDetail />} />
        <Route
          path={"/signup"}
          element={
            <div>
              <Signup updateUser={updateUser}/>
            </div>
          }
        />
        <Route
          path={"/login"}
          element={
            <div>
              <Login updateUser={updateUser}/>
            </div>
          }
        />
        <Route
          path={"/"}
          element={
            <div>
              <Home post={post} />
            </div>
          }
        />
        <Route
          path={"*"}
          element={
            <>
              <h1>Sorry We can't find the Page you're looking for!</h1>
              <h1>404 Not Found</h1>
            </>
          }
        />
      </Routes>
    </>
  );
}

export default App;

