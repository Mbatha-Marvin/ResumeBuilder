import React from 'react'
import ReactDOM from 'react-dom/client'
import Footer from './components/Footer.jsx'


import App from './App.jsx'
import './App.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
    <Footer />
  </React.StrictMode>,
)
