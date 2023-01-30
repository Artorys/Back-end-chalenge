import { ReactElement } from "react";
import { StyledForm } from "./style";

interface IFormProps{
    children: ReactElement;
    onSubmit?: React.FormEventHandler<HTMLFormElement> | undefined
}

export function Form(props : IFormProps){
    return(
        <StyledForm onSubmit={props.onSubmit} encType="multipart/form-data">
            {props.children}
        </StyledForm>
    )
}