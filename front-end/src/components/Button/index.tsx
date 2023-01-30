import { StyledButton } from "./styled";

interface IButtonProps{
    text : string
}

export function Button(props : IButtonProps){
    return(
        <StyledButton type="submit">{props.text}</StyledButton>
    )
}