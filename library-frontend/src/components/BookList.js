import React, { useEffect, useState } from 'react';
import axios from 'axios';

const BookList = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    axios
      .get('https://library-ihd2.onrender.com/books')
      .then(response => {
        console.log('Fetched books:', response.data);
        setBooks(response.data);
      })
      .catch(error => {
        console.error('Error fetching books:', error);
      });
  }, []);

  return (
    <div>
      <h2>Library Contents</h2>
      {books.length === 0 ? (
        <p>No books yet!</p>
      ) : (
        <ul>
          {books.map(book => (
            <li key={book.id}>
              <strong>{book.title}</strong> by {book.author} — {book.status}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default BookList;
