import React, { useState } from 'react';
import axios from 'axios';

// Use your environment variable
const API = process.env.REACT_APP_API_BASE_URL;

const AddBookForm = () => {
  // State for all form inputs
  const [form, setForm] = useState({
    title: '',
    author: '',
    genre: '',
    status: '',
    rating: 0,
    review: '',
    completion_date: ''
  });

  // Update form field when user types
  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // On form submit: send POST to backend
  const handleSubmit = e => {
    e.preventDefault();

    axios.post(`${API}/books`, form)
      .then(() => {
        alert('✅ Book added!');
        setForm({ title: '', author: '', genre: '', status: '', rating: 0, review: '', completion_date: '' });
      })
      .catch(err => alert('❌ Failed to add book: ' + err.message));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add a Book</h2>

      <input name="title" value={form.title} onChange={handleChange} placeholder="Title" required /><br />
      <input name="author" value={form.author} onChange={handleChange} placeholder="Author" required /><br />
      <input name="genre" value={form.genre} onChange={handleChange} placeholder="Genre" /><br />
      <input name="status" value={form.status} onChange={handleChange} placeholder="Status (read/reading/want to read)" required /><br />
      <input name="rating" type="number" value={form.rating} onChange={handleChange} placeholder="Rating (1–10)" /><br />
      <input name="review" value={form.review} onChange={handleChange} placeholder="Review" /><br />
      <input name="completion_date" type="date" value={form.completion_date} onChange={handleChange} /><br />

      <button type="submit">Add Book</button>
    </form>
  );
};

export default AddBookForm;
