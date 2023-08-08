import { useState } from 'react';

function Education() {
  const [collegeName, setCollegeName] = useState('');
  const [startYear, setStartYear] = useState('12/06/2000');
  const [endYear, setEndYear] = useState('10/12/2030');
  
  const [schoolName, setSchoolName] = useState('');
  const [startDate, setStartDate] = useState('12/06/2000');
  const [endDate, setEndDate] = useState('10/12/2030');

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`School Name: ${schoolName}\nStart Date: ${startDate}\nEnd Date: ${endDate}`);
    console.log(`College Name: ${collegeName}\nStart Date: ${startYear}\nEnd Date: ${endYear}`);
  }
  




  return (

<form class="font-monospace" onSubmit={handleSubmit}>
  <div className="grid-container">
    <h3>
      Education Background: 
    </h3>
 
      <label className="grid" name="schoolName">Enter Your School Name:</label>
      <input type="text" id="schoolName" name="schoolName" value={schoolName} onChange={(e) => setSchoolName(e.target.value)} />
    

      <label name="startYear">Start Date:</label>
      <input type="Date" id="startDate" name="startDate" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
      

      <label name="endDate">End Date:</label>
      <input type="Date" id="endDate" name="endDate" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
      <br />

      <label className="grid" name="schoolName">Enter Your College Name:</label>
      <input type="text" id="collegeName" name="collegeName" value={collegeName} onChange={(e) => setCollegeName(e.target.value)} />
    

      <label name="startYear">Start Date:</label>
      <input type="Date" id="startYear" name="startYear" value={startYear} onChange={(e) => setStartYear(e.target.value)} />
      

      <label name="endDate">End Date:</label>
      <input type="Date" id="endYear" name="endYear" value={endYear} onChange={(e) => setEndYear(e.target.value)} />
      <br />

      <button type="submit">Submit</button>
      </div>
    </form>
  )
}

export default Education;