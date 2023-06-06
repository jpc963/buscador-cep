import React from "react"

const InformacaoCep = ({infoCep}) => {

    return (

        <div className="cep-informacao">
            <div className="item-cep">
                <span>CEP</span>
                <span>{infoCep.cep}</span>
            </div>
            <div className="item-cep">
                <span>ESTADO</span>
                <span>{infoCep.state}</span>
            </div>
            <div className="item-cep">
                <span>CIDADE</span>
                <span>{infoCep.city}</span>
            </div>
            <div className="item-cep">
                <span>BAIRRO</span>
                <span>{infoCep.neighborhood}</span>
            </div>
            <div className="item-cep">
                <span>RUA</span>
                <span>{infoCep.street}</span>
            </div>
        </div>

    )
}

export default InformacaoCep