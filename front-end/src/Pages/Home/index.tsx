import { ChangeEvent, useState } from "react";
import { Upload } from "../../components/Upload";
import { Header } from "../../components/Header";
import { StyledDiv, StyledMain, StyledTable, StyledTd } from "./style";
import { api } from "../../api";
import { Description } from "../../components/Description";
import { Button } from "../../components/Button";
import { Form } from "../../components/Form";

interface ICnab{
    cartao: string,
    cpf: string
    data: string
    dono_da_loja: string
    hora : string
    id: number,
    nome_da_loja: string
    tipo: {
        descricao: string,
        id: number,
        natureza: string
        sinal: string
		},
    tipo_id: number,
    valor: string
}

export function Home(){

    const [file,setFile] = useState<File>()
    const [cnab,setCnab] = useState([{} as ICnab])

    return( 
        JSON.stringify(cnab[0]) === "{}" ? <StyledDiv>
            <StyledMain>
                <Header text="Carregue seu arquivo aqui:"></Header>
                <Form onSubmit = {async (eve)=>{
                        eve.preventDefault()
                        if(file){
                            
                            try{
                                const resPost = await api.post("",{cnab : file})
                                if(resPost.status != 200){
                                    throw new Error()
                                }
                                const resGet = await api.get("")
                                setCnab(resGet.data)
                                
                            }
                            catch(err){
                                console.log("erro ao enviar arquivo")
                            }
                            
                        }
                    }}>
                        <>
                            <Upload onChange = {(eve: ChangeEvent<HTMLInputElement>)=>{
                                if(eve.target.files){
                                    const file = eve.target.files[0]
                                    setFile(file)
                                }
                            }} text="Upload"></Upload>
                            <Button text="Enviar"></Button>
                        </>
                </Form>
                <Description text="Arquivo selecionado:"></Description>
                <Description text={file?.name}></Description>
            </StyledMain>
        </StyledDiv>:
               <StyledTable>
            <thead>
             <>
                <tr>
                    <th>Tipo</th>
                </tr>
                 {cnab.map((el : ICnab,index)=>{
                    const tipo = el.tipo
                    return (
                        <tr>
                            <StyledTd>
                                {tipo.descricao}
                            </StyledTd>
                            <StyledTd>
                                {tipo.natureza}
                            </StyledTd>
                            <StyledTd>
                                {tipo.sinal}
                            </StyledTd>
                        </tr>
                    )
                 })}
             </>
        </thead>
        <tbody>
        <>
                <tr>
                    <th>Loja</th>
                </tr>
                 {cnab.map((el : ICnab,index)=>{
                    const nome = el.nome_da_loja
                    return (
                        <tr>
                            <StyledTd>
                                {nome}
                            </StyledTd>
                        </tr>
                    )
                 })}
             </>
        </tbody>
        <tfoot>
            <>
                <tr>
                    <th>Saldo</th>
                </tr>
                 {cnab.map((el : ICnab,index)=>{
                    const valor = el.valor
                    return (
                        <tr>
                            <StyledTd>
                                {valor}
                            </StyledTd>
                        </tr>
                    )
                 })}
             </>
        </tfoot>
     </StyledTable>
    )
}