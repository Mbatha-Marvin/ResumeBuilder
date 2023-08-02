import './App.css'


//import './components/Home/Home.css'
//import 'bootstrap/dist/css/bootstrap.min.css';

import Navbar from "./components/Navbar/Navbar";

//import "./components/Education/Education.css";
//import PersonalDetails from "./components/PersonalDetails"

import Home from "./components/Home/Home.jsx";
//import Education from './components/Education/Education';
//import Skills from './components/Skills/Skills';
import Footer from './components/Navbar/Footer.jsx';
import { Button } from 'react-bootstrap';


function App() {
  return (
    <div className='.bg-danger container'>

      <Navbar />

      <div className='row main-app-container .float-start'>

        <div className='col-md-4'>



          <ul>
            <li ><a href="#home">Home</a></li>
            <li ><a href="#education">Education</a></li>
            <li ><a href="#skills">Skills</a></li>
            <li ><a href="#experience">Experience</a></li>
          </ul>
        </div>
        <div className='col-md-8'>
          <div>
            <Home />
          </div>
          <div>
          </div>
        </div>
      </div>

<Footer />

    </div>
  )
}

export default App;