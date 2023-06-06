import React, {useState} from "react"
import InformacaoCep from "./InformacaoCep.js"

const PesquisaCep = () => {

    let [cep, setCep] = useState('')
    let [infoCep, setInfoCep] = useState()

    let getCep = async () => {
        let response = await fetch(`api/pesquisa/${cep}`)
        let data = await response.json()
        if (data === 'CEP inválido') {
            alert('CEP inválido')
            return
        }
        setInfoCep(data)
    }

    let infoCepComponent = () => {
        if (infoCep !== null && infoCep !== undefined) {
            return <InformacaoCep infoCep={infoCep}/>
        }
    }

    return (

        <div>
            <div className="cep-header">
                <h1>Consulta de CEP</h1>
            </div>
            <div className="cep-buscar">
                <label htmlFor="input-cep">CEP:</label>
                <input type="text" name="input-cep" id="input-cep" placeholder="Somente números" maxLength="8" onChange={(e) => setCep(e.target.value)}/>
                <button className="btn-buscar" onClick={getCep}>Pesquisar</button>
            </div>
            <div>
                {infoCepComponent()}
            </div>
        </div>

    )
}

export default PesquisaCep