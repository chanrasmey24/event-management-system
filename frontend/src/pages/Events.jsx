import { useEffect, useState } from 'react'
import api from '../api'

export default function Events() {
  const [events, setEvents] = useState([])

  const loadEvents = async () => {
    const res = await api.get('/events')
    setEvents(res.data)
  }

  useEffect(() => {
    loadEvents()
  }, [])

  return (
    <div>
      <h2>Events</h2>

      {events.map(e => (
        <div key={e.id} style={{ border: '1px solid #ccc', margin: 10, padding: 10 }}>
          <h3>{e.title}</h3>
          <p>{e.description}</p>
          <p>{e.date}</p>
          <p>{e.location}</p>
        </div>
      ))}
    </div>
  )
}
