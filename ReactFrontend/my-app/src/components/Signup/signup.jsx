import { useState } from 'react';

const SignupForm = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/signup', {
        username,
        email,
        password,
      });
      console.log(response.data.message); // Success message from the backend
      // You can also reset form fields here
    } catch (error) {
      console.error('Error signing up:', error.message);
      // Handle error (show error message to the user, etc.)
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Username:
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </label>
      <label>
        Email:
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </label>

      <label>
        Password:
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </label>


    {  /* ... form inputs ... */}
      <button type="submit">Sign Up</button>
    </form>
  );
};
export default SignupForm;
