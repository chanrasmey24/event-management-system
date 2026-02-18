import { Link } from 'react-router-dom'

export default function Dashboard() {
  return (
    <div>
      <h1>Smart Campus Dashboard</h1>

      <nav>
        <Link to="/events">Events</Link> |{' '}
        <Link to="/admin">Admin</Link>
      </nav>
    </div>
  )
}
