<template>
    
        <header>
            <label for="check">
                <i class="fas fa-bars" id="hamburguer"></i>
            </label>
            <div class="left-area">
                <h3>Coding <span>Snow</span></h3>
            </div>
            <div class="right-area">
                <a href="#" class="logout-btn"
                    >Logout <i class="fas fa-sign-out-alt"></i
                ></a>
            </div>
        </header>
        <div class="sidebar">
            <center>
                <img src="assets/rosto-mulher.jpg" class="profile-img" alt="" />
                <h4>Mary da Silva</h4>
            </center>
            <nav>
                <NuxtLink to="/resume/start">Lets start</NuxtLink>
                <NuxtLink to="/resume/profile"><i class="bi bi-person"></i>{{' '}}Profile</NuxtLink>
                <NuxtLink to="/resume/education"><i class="bi bi-book"></i>{{' '}}Education</NuxtLink>
                <NuxtLink to="/resume/experience"><i class="bi bi-list-stars"></i>{{' '}}Experience</NuxtLink>
                <NuxtLink to="/resume/language"><i class="bi bi-translate"></i>{{' '}}Languages</NuxtLink>
                <NuxtLink to="/resume/certification"><i class="bi bi-patch-check"></i>{{' '}}Certification</NuxtLink>
                <NuxtLink to="/resume/project"><i class="bi bi-blockquote-left"></i>{{' '}}Projects</NuxtLink>
                <NuxtLink to="/resume/referee"><i class="bi bi-sliders2"></i>{{' '}}Referees</NuxtLink>
                <NuxtLink to="/template"><i class="bi bi-eye-fill"></i>{{' '}}Preview</NuxtLink>
            </nav>
        </div>

        <div class="content">
            <div class="wrapper">
                <slot />
            </div>
        </div>
</template>

<script>

</script>

<style scoped>

</style>