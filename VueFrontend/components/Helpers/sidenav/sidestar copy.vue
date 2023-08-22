<template>

     <div class="wrapper" >
<div class="side-navigation" >
        <!-- Sidebar content goes here -->
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
        <!-- Main content goes here -->
           <slot />
  </div>
</div>
</template>

<script>

</script>

<style scoped>

body {
  margin: 0;
  font-family: "Lato", sans-serif;
}
.wrapper {
  display: flex;
  min-height: 100vh;
}

.side-navigation {
  width: 250px;
  background-color: #333;
  padding-top: 60px;
  flex: 0 0 250px;
  transition: 0.5s;
  overflow-y: auto;
}

.side-navigation a {
  padding: 15px 25px;
  text-align: center;
  text-decoration: none;
  font-size: 18px;
  color: white;
  display: block;
  transition: 0.3s;
}

.side-navigation a:hover {
  background-color: #555;
}

.content {
  flex: 1;
  padding: 20px;
}

@media screen and (max-width: 768px) {
  .wrapper {
    flex-direction: column;
  }
  
  .side-navigation {
    width: 100%;
    height: auto;
  }
  
  .content {
    padding: 20px;
  }
  
  .horizontal-layout {
  flex-direction: row;
}

.side-navigation {
  /* ... existing styles ... */
  flex-direction: column;
}

.show {
  transform: translateX(0);
}

}

</style>