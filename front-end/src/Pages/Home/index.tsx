import { ChangeEvent, useState } from "react";
import { Upload } from "../../components/Upload";
import { Header } from "../../components/Header";
import { StyledDiv, StyledMain } from "./style";
import { api } from "../../api";
import { Description } from "../../components/Description";
import { Button } from "../../components/Button";
import { Form } from "../../components/Form";

export function Home(){

    const [file,setFile] = useState<File>()

    return( 
        <StyledDiv>
            <StyledMain>
            <Header text="Carregue seu arquivo aqui:"></Header>
            <Form onSubmit = {async (eve)=>{
                eve.preventDefault()
                if(file){
                    const res = await api.post("",{cnab : file})
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
            {file ? 
            <table>
                
            </table>
            :
            <>

            </>}
            </StyledMain>
        </StyledDiv>
    )
}