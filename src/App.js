import {useState} from 'react'
import axios from 'axios'
import './App.css';


const App = () => {
  const [query, setQuery] = useState('')
  const [imgIdxs, setImgIdxs] = useState([])
  const querySet = (event) => {
    event.preventDefault()
    setQuery(event.target.value)
  }
  const sendQuery = (event) => {
    event.preventDefault()
    const request = axios.get(`http://10.251.100.11:3001/search?query=${query}`)
    request.then(response => setImgIdxs(response.data))
    console.log(imgIdxs)
    console.log(typeof imgIdxs)
  }
        function importAll(r) {
         let images = {};
          r.keys().forEach((item, index) => { images[item.replace('./', '')] = r(item); });
         return images
        }
        const images = importAll(require.context('./static', false, /\.(png|jpe?g|svg)$/));
  return (
    <div className="App">
      <header className="App-header">
        <h1>SST</h1>
        <input onChange={querySet} />
        <button onClick={sendQuery}>
          Искать
        </button>
          {imgIdxs.map(im_id => <img src={images[`${im_id}_main_gen.jpg`]} alt={`${im_id}im`} height={150} width={150}/>)}
      </header>
    </div>
  );
}

export default App;
