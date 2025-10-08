import React, { useState } from "react";
import axios from "axios";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/users/login", {
        username,
        password
      });
      setToken(response.data.access_token);
      alert("Login successful! Token: " + response.data.access_token);
    } catch (error) {
      alert("Login failed: " + error.response.data.detail);
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <input placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <input placeholder="Password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button type="submit">Login</button>
      </form>
      {token && <p>JWT Token: {token}</p>}
    </div>
  );
}

export default Login;
// After login success
localStorage.setItem("token", response.data.access_token);
