import {BrowserRouter as Routers, Routes, Route} from "react-router-dom"
import './App.css'
import PesquisaCep from './components/PesquisaCep.js'

function App() {

    return (

        <div className="container dark">
            <Routers>
                <div className="app">
                    <Routes>
                        <Route path="/" element={<PesquisaCep/>}/>
                    </Routes>
                </div>
            </Routers>
        </div>

    )
}

export default App
