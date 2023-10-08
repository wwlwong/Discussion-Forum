import { useFormik } from "formik";
import * as Yup from "yup";
import "./App.css";
import { useState } from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";

const SignUpSchema = Yup.object().shape({
    username: Yup.string().required("Username is required"),
    password: Yup.string().required("Password is required"),
    email: Yup.string().email().required("Email is required"),    
});

function Signup() {
    
    const [signUp, setSignUp] = useState(false);
    const [userData, setUserData] = useState({
        name: "",
        email: "",
        password: "",
    });
    
    

    const handleOnSubmit = (e) => {
        e.preventDefault();
        const config = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(
            signUp ? userData : { name: userData.name, password: userData.password, email: userData.email }
          ),
        };
    }

    const formik = useFormik({
        initialValues: {
          username: "",
          password: "",
          email: "",
        },
        validationSchema: schema,
        onSubmit: handleOnSubmit,
      });

    const setInputValue = useCallback(
        (key, value) =>
            formik.setValues({
            ...formik.values,
            [key]: value,
            }),
        [formik]
    );

    return (
        <form onSubmit={formik.handleSubmit}>
          <input
            placeholder="Type your userame"
            value={formik.values.username}
            onChange={(e) => setInputValue("username", e.target.value)}
          />
          <small>{formik.errors.userame}</small>
          <input
            placeholder="Type your password"
            value={formik.values.password}
            onChange={(e) => setInputValue("password", e.target.value)}
          />
          <small>{formik.errors.password}</small>
          <input
            placeholder="Type your email"
            value={formik.values.email}
            onChange={(e) => setInputValue("email", e.target.value)}
          />
          <small>{formik.errors.email}</small>
          {!!formik.errors.password && <br />}
          <button type="submit" disabled={!formik.isValid}>
            Submit
          </button>
        </form>
      );


}

export default Signup;
