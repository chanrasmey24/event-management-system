import { Navigate, Outlet } from 'react-router-dom'

export default function ProtectedRoute({ requiredRole }) {
  const token = localStorage.getItem('token')
  const role = localStorage.getItem('role')

  if (!token) return <Navigate to="/login" />

  if (requiredRole && role !== requiredRole) {
    return <Navigate to="/" />
  }

  return <Outlet />
}

