import React, {StrictMode} from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'
import './styles/global.css'

const container = document.getElementById('root') as HTMLDivElement;

createRoot(container).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
