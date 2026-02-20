import { Link } from 'react-router-dom'

export default function Navbar() {
  return (
    <nav style={{ marginBottom: 20 }}>
      <Link to="/">Dashboard</Link> |{' '}
      <Link to="/events">Events</Link> |{' '}
      <Link to="/my-registrations">My Registrations</Link> |{' '}
      <Link to="/admin">Admin</Link> |{' '}
      <button onClick={() => {
        localStorage.clear()
        window.location.href = '/login'
      }}>Logout</button>
    </nav>
  )
}
