<template>
  <div class="sidebar">
    <NuxtLink to="/resume/start">Lets start</NuxtLink>
        <NuxtLink to="/resume/profile"><i class="bi bi-person"></i>{{' '}}Profile</NuxtLink>
        <NuxtLink to="/resume/education"><i class="bi bi-book"></i>{{' '}}Education</NuxtLink>
        <NuxtLink to="/resume/experience"><i class="bi bi-list-stars"></i>{{' '}}Experience</NuxtLink>
        <NuxtLink to="/resume/language"><i class="bi bi-translate"></i>{{' '}}Languages</NuxtLink>
        <NuxtLink to="/resume/certification"><i class="bi bi-patch-check"></i>{{' '}}Certification</NuxtLink>
        <NuxtLink to="/resume/project"><i class="bi bi-blockquote-left"></i>{{' '}}Projects</NuxtLink>
        <NuxtLink to="/resume/referee"><i class="bi bi-sliders2"></i>{{' '}}Referees</NuxtLink>
        <NuxtLink to="/template"><i class="bi bi-eye-fill"></i>{{' '}}Preview</NuxtLink>
  </div>
  <div class="content">
              <slot />
      </div>
  </template>
  
  <script>
  
  </script>
  
  <style>
  body {
    font-family: "Lato", sans-serif;
  }
  
  .sidebar {
    margin: 0;
    padding: 0;
    width: 200px;
    background-color: #f1f1f1;
    position: fixed;
    height: 100%;
    overflow: auto;
  }
  
  .sidebar a {
    display: block;
    color: black;
    padding: 16px;
    text-decoration: none;
  }
   
  .sidebar a.active {
    background-color: #04AA6D;
    color: white;
  }
  
  .sidebar a:hover:not(.active) {
    background-color: #555;
    color: white;
  }
  
  div.content {
    margin-left: 200px;
    padding: 1px 16px;
    height: 1000px;
  }
  
  @media screen and (max-width: 700px) {
    .sidebar {
      width: 100%;
      height: auto;
      position: fixed;
    }
    .sidebar a {float: left;}
    div.content {margin-left: 0;}
  }
  
  @media screen and (max-width: 400px) {
    .sidebar a {
      text-align: center;
      float: none;
    }
  }
  </style>