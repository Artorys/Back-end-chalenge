import {StyledForm, StyledInput, StyledLabel} from "./style"

interface IUploadProps{
    text: string
    onChange?: React.ChangeEventHandler<HTMLInputElement> | undefined

}

export function Upload(props : IUploadProps){
    return( 
        <>
            <StyledLabel htmlFor = "upload">{props.text}</StyledLabel>
            <StyledInput id="upload" onChange={props.onChange} type={"file"}></StyledInput>
        </>
    )
}