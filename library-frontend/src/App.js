import React from 'react';
import BookList from './components/BookList';
import AddBookForm from './components/AddBookForm';

function App() {
  return (
    <div style={{ padding: '2rem' }}>
      <h1>📚 My Library</h1>
      <AddBookForm />
      <hr />
      <BookList />
    </div>
  );
}

export default App;
