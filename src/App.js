import {useState} from 'react'
import './App.css';

const App = () => {
  const [query, setQuery] = useState('')
  const querySet = (event) => {
    event.preventDefault()
  }
  return (
    <div className="App">
      <header className="App-header">
        <h1>SST</h1>
        <input onChange />
      </header>
    </div>
  );
}

export default App;
