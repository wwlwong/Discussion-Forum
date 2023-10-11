import React, { useState } from "react";
import { useHistory } from "react-router-dom";

const NewPostForm = ({ addPost }) => {
  const history = useHistory();
  const [postData, setPostData] = useState({
    title: "",
    link: "",
    expiry: "",
    retailer: "",
    category: "",
    content: "",
  });

  const handleChange = ({ target }) => {
    const { name, value } = target;
    const postDataCopy = { ...postData };
    postDataCopy[name] = value;
    setPostData(postDataCopy);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const config = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(postData),
    };

    fetch("/post", config).then((res) => {
      if (res.ok) {
        res.json().then((post) => {
          addPost(post);
          history.push(`/post/${post.id}`);
        });
      }
    });
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label>Title </label>
        <input
          type="text"
          name="title"
          value={postData.title}
          onChange={handleChange}
          required
        />

        <label> Link</label>
        <input
          type="text"
          name="link"
          value={ppostData.link}
          onChange={handleChange}
          required
        />

        <label>Expiry</label>
        <input
          type="text"
          name="expiry"
          value={postData.expiry}
          onChange={handleChange}
          required
        />

        <label>Retailer</label>
        <input
          type="text"
          name="retailer"
          value={postData.retailer}
          onChange={handleChange}
          required
        />

        <label>Category</label>
          <select className="dropdown" 
            name="category" 
            value={postData.category} 
            onChange={handleChange}>
                  <option value="" selected disabled="true">Select Category</option>
                  <option value='Apparel'>Apparel</option>
                  <option value="Automotive">Automotive</option>
                  <option value="Children">Children</option>
                  <option value="Computer and Electronics">Computer and Electronics</option>
                  <option value="Entertainment">Entertainment</option>
                  <option value="Finance">Finance</option>
                  <option value="Food">Food</option>
                  <option value="Home and Garden">Home and Garden</option>
                  <option value="Sports and Fitness">Sports and Fitness</option>
                  <option value="Travel">Travel</option>
              </select>
                      
        <input
          type="text"
          name="director"
          value={postData.director}
          onChange={handleChange}
          required
        />

        <label>Content</label>
        <textarea
          type="text"
          rows="4"
          cols="50"
          name="content"
          value={postData.content}
          onChange={handleChange}
          required
        />

        <input type="submit" />
      </form>
    </div>
  );
};

export default NewPostForm;