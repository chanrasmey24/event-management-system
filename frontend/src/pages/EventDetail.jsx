import { useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'
import api from '../api'

export default function EventDetail() {
  const { id } = useParams()
  const [event, setEvent] = useState(null)

  useEffect(() => {
    const load = async () => {
      const res = await api.get(`/events/${id}`)
      setEvent(res.data)
    }
    load()
  }, [id])

  if (!event) return <p>Loading...</p>

  return (
    <div>
      <h2>{event.title}</h2>
      <p>{event.description}</p>
      <p>{event.date}</p>
      <p>{event.location}</p>
    </div>
  )
}
