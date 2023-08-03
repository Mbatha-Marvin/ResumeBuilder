
const Skills = () => {
  return (
    <div className="skills-container">
      <strong>Skills</strong>
      <form>
  { /* 2 column grid layout with text inputs for the first and last names */ }
  <div className="row mb-4">
    <div className="col">
      <div className="form-outline">
        <input type="text" id="form3Example1" className="form-control" />
        <label className="form-label" htmlFor="form3Example1">First name</label>
      </div>
    </div>
    <div className="col">
      <div className="form-outline">
        <input type="text" id="form3Example2" className="form-control" />
        <label className="form-label" htmlFor="form3Example2">Last name</label>
      </div>
    </div>
  </div>

  { /* Email input */ }
  <div className="form-outline mb-4">
    <input type="email" id="form3Example3" className="form-control" />
    <label className="form-label" htmlFor="form3Example3">Email address</label>
  </div>

  { /* Password input */ }
  <div className="form-outline mb-4">
    <input type="password" id="form3Example4" className="form-control" />
    <label className="form-label" htmlFor="form3Example4">Password</label>
  </div>

  { /* Submit button */ }
  <button type="submit" className="btn btn-primary btn-block mb-4">Sign up</button>

  { /* Register buttons */ }
  <div className="text-center">
    <p>or sign up with:</p>
    </div>
</form>
    
    </div>
  )
}

export default Skills