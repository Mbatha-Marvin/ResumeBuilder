import { useState } from "react";

function Home() {
  const [formData, setFormData] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log("Form data submitted: ", formData);
  };

  return (
    <div className="Home-container">
      <h1>Personal Information</h1>
      <hr />

      {/* <img src="cinqueterre.jpg" className="rounded" alt="Cinque Terre" />
      <form onSubmit={handleSubmit}>
        <label>Profile Picture</label>
        <input
          type="image"
          name="profilePicture"
          value={formData.profilePicture}
          onChange={handleChange}
          required
          />

      /* <form onSubmit={handleSubmit}>
        <label>Name</label>
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
        />

        <br />
        <label>Email</label>
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          required
        />

        <br />
        <label>Location:</label>
        <input
          type="text"
          name="location"
          value={formData.location}
          onChange={handleChange}
          required
        />
        <br />

        <label>Website Link</label>
        <input
          type="link"
          name="website-link"
          value={formData.link}
          onChange={handleChange}
          required
        />
        <br />

        <label>Github Link</label>
        <input
          type="text"
          name="github-link"
          value={formData.githublink}
          onChange={handleChange}
          required
        />
        <br />


        <button type="submit">Submit</button>
        <br /> */}

      <form onSubmit={handleSubmit}>
        {/* 2 column grid layout with text inputs for the first and last names */}
        <div className="row mb-4">
          <div className="col">
            <div className="form-outline">
              <label className="form-label" htmlFor="form6Example1">
                First name
              </label>
              <input
                type="text"
                name="firstname"
                value={formData.firstname}
                onChange={handleChange}
                required
                id="form6Example1"
                className="form-control"
              />

            </div>
          </div>
          <div className="col">
            <div className="form-outline">
              <label className="form-label" htmlFor="form6Example2">
                Last name
              </label>
              <input
                type="text"
                name="lastname"
                value={formData.lastname}
                onChange={handleChange}
                required
                id="form6Example1"
                className="form-control"
              />

            </div>
          </div>
        </div>

        {/* Email input */}
        <div className="form-outline mb-4">
          <label className="form-label" htmlFor="form6Example5">
            Email
          </label>          
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            id="form6Example5"
            className="form-control"
          />

        </div>

        {/* Number input */}
        <div className="form-outline mb-4">
          <label className="form-label" htmlFor="form6Example6">
            Phone
          </label>
          <input
            type="number"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
            required
            id="form6Example6"
            className="form-control"
          />

        </div>

        {/* Text input */}
        <div className="form-outline mb-4">
          <label className="form-label" htmlFor="form6Example4">
            Address
          </label>
          <input
            type="text"
            name="address"
            value={formData.address}
            onChange={handleChange}
            required
            id="form6Example3"
            className="form-control"
          />

        </div>

        {/* Text input */}
        <div className="form-outline mb-4 bg">
          <label className="form-label" htmlFor="form6Example3">
            Location
          </label>
          <input
            type="text"
            name="location"
            value={formData.location}
            onChange={handleChange}
            required
            id="form6Example3"
            className="form-control"
          />

        </div>

        <div className="form-outline mb-4">
          <label className="form-label" htmlFor="form6Example3">
            Website Link
          </label>
          <input
            type="text"
            name="websiteLink"
            value={formData.websiteLink}
            onChange={handleChange}
            required
            id="form6Example3"
            className="form-control"
          />

        </div>

        {/* Submit button */}
        <button type="submit" className="btn btn-primary btn-block mb-4">
          Submit Details
        </button>
      </form>


      <div className="container">
        <h2 className="strong">Personal Information data</h2>
        <div className="list-group .md-strong">
          <div>
            <span className="list-group-item .strong">First Name: {formData.firstname}</span>
          </div>
          <div>
            <span className="list-group-item .strong">Last Name: {formData.lastname}</span>
          </div>
          <div>
            <span className="list-group-item .strong">Email: {formData.email}</span>
          </div>
          <div>
            <span className="list-group-item .strong">Phone: {formData.phone}</span>
          </div>
          <div>
            <span className="list-group-item .strong">Address: {formData.address}</span>
          </div>
          <div>
            <span className="list-group-item .strong">Location: {formData.location}</span>
          </div>
          <div>
            <span className="list-group-item .strong">Website Link: {formData.websiteLink}</span>
          </div>

          <button type="submit" className="btn btn-primary btn-block mb-4">
          Edit
        </button>
        </div>
      </div>
    </div>

  );
}

export default Home;
