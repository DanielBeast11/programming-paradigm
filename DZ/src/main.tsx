import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import Converter from './components/Converter.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Converter />
  </StrictMode>,
)
