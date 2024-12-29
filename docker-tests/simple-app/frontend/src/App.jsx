import { useState } from 'react'
import './App.css'

function App() {
  const [inputText, setInputText] = useState('')
  const [resultText, setResultText] = useState('')

  const handleInputChange = (e) => {
    setInputText(e.target.value)
  }

  const apiURL = `http://localhost:8000/?user_message=${inputText}`;

  const handleSubmit = async () => {
    try {
      const response = await fetch(apiURL, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        }
      })
      const data = await response.json()
      console.log(data)
      setResultText(data.result)
    } catch (error) {
      console.error('Error:', error)
    }
  }

  return (
    <>
      <div>
        <input
          type="text"
          value={inputText}
          onChange={handleInputChange}
          placeholder="Enter text"
        />
        <button onClick={handleSubmit}>Submit</button>
      </div>
      {resultText && <div>Result: {resultText}</div>}
    </>
  )
}

export default App