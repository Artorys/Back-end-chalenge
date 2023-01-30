import { StyledHeader } from "./style";

interface IHeaderProps{
    text: string
}

export function Header(props : IHeaderProps){
    return( 
        <StyledHeader>{props.text}</StyledHeader>
    )
}