import { useEffect, useState } from 'react'
import api from '../api'

export default function MyRegistrations() {
  const [registrations, setRegistrations] = useState([])

  useEffect(() => {
    const load = async () => {
      const res = await api.get('/registrations')
      setRegistrations(res.data)
    }
    load()
  }, [])

  return (
    <div>
      <h2>My Registrations</h2>

      {registrations.map(r => (
        <div key={r.id}>
          <p>Event ID: {r.event_id}</p>
        </div>
      ))}
    </div>
  )
}