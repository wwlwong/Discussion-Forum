import React from 'react';
import { Formik, Field, Form, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
 
const Signup = ({user, handleAccount}) => {
  const [errorPage, setErrorPage] = useState("");
  const history = useHistory();
  const formik = useFormik({
    initialValues: {
      username: '',
      password: '',
      email: '',
    },
    validationSchema: Yup.object({
      username: Yup.string()
        .required('Username Required'),
      password: Yup.string()
        .required('Password Required'),
      email: Yup.string().email('Invalid email address').required('Email Address Required'),
    }),
    onSubmit: values => {
      fetch(`signup`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values, null, 2),
        }).then((res) => {
          console.log(res);

          if (res.ok) {
            setErrorPage("Successfully signed up");
            res.json().then((user) => {
              handleAccount(user);
            });
            history.push(`/login`);
          } else if (res.status === 400) {
            setErrorPage("Username already exists");
          }
        });
      },
  
    if (user) {
      return <h1>Welcome!</h1>;
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

      <label htmlFor="email">Email Address</label>
      <input
        id="email"
        name="email"
        type="email"
        onChange={formik.handleChange}
        onBlur={formik.handleBlur}
        value={formik.values.email}
      />
      {formik.touched.email && formik.errors.email ? (
        <div>{formik.errors.email}</div>
      ) : null}

      <button type="submit">Submit</button>
    </form>
  );
};

 export default Signup