import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import './App.css'
import * as bootstrap from 'bootstrap' ;
import 'bootstrap-icons/font/bootstrap-icons.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Home from './components/Home/Home.jsx'
import Skills from './components/Skills/Skills.jsx';
import Education from './components/Education/Education.jsx';
import Signup from './components/Signup/signup.jsx';
import Api from './components/Signup/Api.jsx';
//import { createBrowserRouter } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path:'/',
    element:<App />,
    errorElement:<h1>Page not found</h1>,
  
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/skills",
        element: <Skills />,
      },
      {
        path: "/education",
        element: <Education />,
      },
      {
        path: "/signup",
        element: <Signup />,
      },
      {
        path: "/api",
        element: <Api />,
      },
  {
    path: "*",
    element: <div>ErrorPage</div>,
  }
]
}])


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
     <RouterProvider router={router} />
  </React.StrictMode>
)
