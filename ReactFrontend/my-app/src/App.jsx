import './App.css'
import { Link, Outlet } from 'react-router-dom';
//import Footer from './components/Footer'

//import './components/Home/Home.css'
//import 'bootstrap/dist/css/bootstrap.min.css';

import Navbar from "./components/Navbar/Navbar";

//import "./components/Education/Education.css";
//import PersonalDetails from "./components/PersonalDetails"

//import Home from "./components/Home/Home.jsx";
//import Education from './components/Education/Education';
//import Skills from './components/Skills/Skills';
import Footer from './components/Navbar/Footer.jsx';
import { Button } from 'react-bootstrap';
import SignupForm from './components/Signup/signup';


function App() {
  return (
    <div className='container'>

      <Navbar />

      <div className='row main-app-container .float-start'>

        <div className='col-md-4'>
          <ul>
            <li >
              <Link to="/">Home</Link>
              </li>
            <li>
              <Link to="/skills">Skills</Link>
            </li>
            <li>
              <Link to="/education">Education</Link>
            </li>
            <li>
            <Link to="/signup">Signup</Link>
            </li>
            <li>
            <Link to="/api">Api</Link>
            </li>
          </ul>
        </div>
        <div className='col-md-8'>
          {/* <div>
            <Home />
          </div>
          
          <div>
            <Skills />
          </div> */}
          {/* <div>
            <Education />
          </div> */}
          {/* <div>
            <SignupForm />
          </div> */}
          {/* <div>
            <Api />
          </div> */}
          <Outlet />
        </div>
      </div>
<Footer />
    </div>
  )
}

export default App;