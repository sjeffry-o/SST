import {useState} from 'react'
import axios from 'axios'
import './App.css';

const App = () => {
  const [query, setQuery] = useState('')
  const querySet = (event) => {
    event.preventDefault()
    setQuery(event.target.value)
  }
  const sendQuery = (event) => {
    event.preventDefault()
    const request = axios.get(`http://127.0.0.1:5000/search?query=${query}`)
    const data = request.then(response => response.data)
    console.log(data)
  }
  return (
    <div className="App">
      <header className="App-header">
        <h1>SST</h1>
        <input onChange={querySet} />
        <button onClick={sendQuery}>
          Искать
        </button>
      </header>
    </div>
  );
}

export default App;
