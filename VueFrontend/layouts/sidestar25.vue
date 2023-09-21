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
        <NuxtLink to="/resume/preview"><i class="bi bi-eye-fill"></i>{{' '}}Preview</NuxtLink>
    </div>
    <div class="main py-4 d-flex justify-contents-center"> 
            <slot />
    </div>

</template>

<script>

export default {
  data() {
    return {
      isOpen: false,
    };
  },
  methods: {
    toggleSidebar() {
      this.isOpen = !this.isOpen;
    },
  },
};

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
    background-color: #555;
}

.router-link-exact-active {
    color: #f1f1f1 !important;
    background-color: #440f58;
    border-color: #140266;
}

.main {
    margin-left: 150px;
    font-family: "Lato", sans-serif;
    font-size: 14px;
    padding: 0px 0px;
}

@media (max-width: 768px) {
    .sidenav {
        padding-top: 15px;
    }

    .sidenav a {
        font-size: 18px;
    }
            
    .router-link-exact-active {
    color: #f1f1f1 !important;
    background-color: #440f58;
    border-color: #140266;
}
}
</style>