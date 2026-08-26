import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [apiMessage, setApiMessage] = useState('Loading...')
  const [error, setError] = useState('')

  useEffect(() => {
    const fetchApiMessage = async () => {
      try {
        const response = await fetch('http://localhost:8000/health')

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }

        const data = await response.json()
        setApiMessage(data.status)
      } catch (err) {
        setError('Unable to connect to the FastAPI backend.')
        console.error(err)
      }
    }

    fetchApiMessage()
  }, [])

  return (
    <main style={{ fontFamily: 'sans-serif', padding: '2rem' }}>
      <h1>ORGINTEL</h1>
      <p>{error || `API status: ${apiMessage}`}</p>
    </main>
  )
}

export default App
