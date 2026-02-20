import { Link } from 'react-router-dom'
import Navbar from '../components/Navbar'

export default function Dashboard() {
  return (
    <div>
      <Navbar />
      <h1>Smart Campus Dashboard</h1>

      <nav>
        <Link to="/events">Events</Link> |{' '}
        <Link to="/admin">Admin</Link>
      </nav>
    </div>
  )
}
