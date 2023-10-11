import React from 'react';
import { Formik, Field, Form, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
 
const Login = ({user, updateUser}) => {
  const [errorPage, setErrorPage] = useState("");
  const history = useHistory();
  const formik = useFormik({
    initialValues: {
      username: '',
      password: '',
    },
    validationSchema: Yup.object({
      username: Yup.string().required('Username Required'),
      password: Yup.string().required('Password Required'),
    }),
    onSubmit: values => {
      fetch(`login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values, null, 2),
        }).then((res) => {
          console.log(res);

          if (res.ok) {
            setErrorPage("Successfully logged in");
            res.json().then((user) => {
              updateUser(user);
            });
            history.push(`/home`);
          } else if (res.status === 422) {
            setErrorPage("Incorrect username and/or password");
          }
        });
      },
  
    if (user) {
      return <h1>Welcome Back!</h1>;
    }
    });

  return (
    <form onSubmit={formik.handleSubmit}>
      <label htmlFor="username">Username</label>
      <input
        id="username"
        name="username"
        type="text"
        onChange={formik.handleChange}
        onBlur={formik.handleBlur}
        value={formik.values.username}
      />
      {formik.touched.username && formik.errors.username ? (
        <div>{formik.errors.username}</div>
      ) : null}

      <label htmlFor="password">Password</label>
      <input
        id="password"
        name="password"
        type="text"
        onChange={formik.handleChange}
        onBlur={formik.handleBlur}
        value={formik.values.password}
      />
      {formik.touched.password && formik.errors.password ? (
        <div>{formik.errors.password}</div>
      ) : null}

      <button type="submit">Submit</button>
    </form>
  );
};

 export default Login