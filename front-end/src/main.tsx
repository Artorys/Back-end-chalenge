import React from 'react'
import ReactDOM from 'react-dom/client'
import { App } from './app'
import { StyledGlobal } from './global/style'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <StyledGlobal></StyledGlobal>
    <App></App>
  </React.StrictMode>
)
