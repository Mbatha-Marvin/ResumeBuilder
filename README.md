Resume Builder
==========

An Open source software founded by [Marvin Mbatha][marvinmbatha], [Ronald Kimeli][ronaldkimeli] and [Robert Kimaiyo][robertkimaiyo] who are aspiring to bring a new phase of Resume builder techs into unlocking jobs with brilliant and ATS friendly Resumes. Your contribution is great inspiration and it is highly encouraged.

Frontend Git branches
-----------------

* AngularFrontend - Based on angular framework.
* ReactFrontend - Based on React framework.
* VueFrontend - Based on Vue framework.

Backend Git Branch
------------------

* FastApiBackend - Is the main high performing backend which is fully API driven.

Table of Contents
-----------------

* [Requirements](#requirements)
* [Usage](#usage)

Requirements
------------

Resume Builder Frontend requirements based on React:

* [Node.js][node] 16+
* [Vite][vite]
* [React Bootrsap][react_bootstrap]
* [Docker][docker]
* [React Router][react_router_dom]
* [Axios][axios]
* [React Toastify][toastify]

[node]: https://nodejs.org
[vite]: https://vitejs.dev
[react_bootstrap]: https://react-bootstrap.netlify.app
[docker]: https://www.docker.com
[react_router_dom]: https://reactrouter.com
[axios]: https://axios-http.com/docs/intro
[toastify]: https://fkhadra.github.io/react-toastify/introduction
[ronaldkimeli]: https://github.com/KimelirR
[marvinmbatha]: https://github.com/Mbatha-Marvin/
[robertkimaiyo]: https://github.com/robert5313


Usage
------------

Clone this repository then create .env for db connection creadentials 


```bash
cd FastApiBackend
```

Make .env from copy of example.env


```bash
cp example.env .env
```

Replace the credentials of db with your favorite naming to be generated with the postrgres 


```bash
DB_USER: DB UserName
DB_PASSWORD: DB Password
DB_NAME: DB Name
```

Install necessary dependencies and run the software servers on detached mode using command below.


```bash
docker compose build --no-cache && docker compose up -d
```
- Fill your data in to be reused on the resume preview e.g set Profile, Education,Certifications, Referees etc
- Preview your details as resume and generate pdf by clicking the pdf logo

* Now check your terminal if everything is already started - On your browser at the url `http://localhost:5173/` if frontend and `http://localhost:5000/` is backend


