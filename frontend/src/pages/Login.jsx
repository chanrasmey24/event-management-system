import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../api'

export default function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  const handleLogin = async e => {
    e.preventDefault()
    try {
      const res = await api.post('/auth/login', {
        email: email,
        password: password
      })

      localStorage.setItem('token', res.data.access_token)
      navigate('/')
    } catch (err) {
      console.log('Login error:', err.response?.data)
      alert('Login failed')
    }
  }

  return (
    <div style={{ maxWidth: 300, margin: '100px auto' }}>
      <h2>Login to AIMs</h2>
      <form onSubmit={handleLogin}>
        <input 
          type="email"
          placeholder="Email" 
          value={email}
          onChange={e => setEmail(e.target.value)} 
          required
          style={{ width: '100%', padding: '8px', marginBottom: '10px' }}
        />
        <input 
          type="password" 
          placeholder="Password" 
          value={password}
          onChange={e => setPassword(e.target.value)} 
          required
          style={{ width: '100%', padding: '8px', marginBottom: '10px' }}
        />
        <button 
          type="submit"
          style={{ width: '100%', padding: '10px', background: '#007bff', color: 'white', border: 'none' }}
        >
          Login
        </button>
      </form>
    </div>
  )
}