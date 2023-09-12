<template>
    <div class="sidenav">
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
    <div class="main py-4 d-flex justify-contents-center">
            <slot />
    </div>
</template>

<script>

</script>

<style scoped>
body {
    font-family: "Lato", sans-serif;
}

.sidenav {
    height: 100%;
    width: 150px;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #0491a3;
    overflow-x: hidden;
    padding-top: 20px;
}


.sidenav a {
  display: block;
  color: black;
  padding: 16px;
  text-decoration: none;
}

.sidenav a:hover {
    color: #f1f1f1;
}

.sidenav a.active {
  background-color: #04AA6D;
  color: white;
}


.sidenav a:hover:not(.active) {
  background-color: #555;
  color: white;
}

.main {
    margin-left: 150px;
    font-family: "Lato", sans-serif;
    /* font-family: "Times New Roman", Times, serif; */
    /* Same as the width of the sidenav */
    font-size: 14px;
    /* Increased text to enable scrolling */
    padding: 0px 0px;
    /* background-color: #555;
    background-size: cover; */
}

@media screen and (max-height: 450px) {
    .sidenav {
        padding-top: 15px;
    }

    .sidenav a {
        font-size: 18px;
    }
}
</style>