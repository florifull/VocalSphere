import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [users, setUsers] = useState([]);

  // Function to handle adding a new user
  const handleAddUser = async () => {
    const userData = { name: 'Jane Doe', email: 'janedoe@example.com' };

    try {
      const response = await axios.post('http://localhost:5000/add', userData, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      console.log(response.data.message); // Log success message
      loadUsers(); // Reload users after adding
    } catch (error) {
      console.error('Error adding user:', error);
    }
  };

  // Function to load users from backend
  const loadUsers = async () => {
    try {
      const response = await axios.get('http://localhost:5000/users');
      setUsers(response.data); // Set the users into state
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  };

  // Fetch users on component mount
  useEffect(() => {
    loadUsers();
  }, []);

  return (
    <div>
      <h1>User List</h1>
      <ul>
        {users.map(user => (
          <li key={user._id}>
            {user.name} - {user.email}
          </li>
        ))}
      </ul>
      <button onClick={handleAddUser}>Add User</button>
    </div>
  );
};

export default App;
