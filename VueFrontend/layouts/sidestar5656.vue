<template>
    <!-- <div class="main py-2 d-flex justify-contents-center">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <div class="card">
                        <div class="card-content collapse show">
                            <div class="card-body card-dashboard">
                                <div class="row">
                                    <button class="btn btn-sm btn-outline-danger float-start" @click="toggleSidebar">
                                        <i class="bi bi-list"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div> -->


    <div class="sidenav" :class="{ 'sidenav-open': sidebarOpen, 'sidenav-closed': !sidebarOpen }">
        <NuxtLink to="/resume/start"><i class="bi bi-grid"></i>{{ ' ' }}Dashboard</NuxtLink>
        <NuxtLink to="/resume/profile"><i class="bi bi-person"></i>{{ ' ' }}Profile</NuxtLink>
        <NuxtLink to="/resume/education"><i class="bi bi-book"></i>{{ ' ' }}Education</NuxtLink>
        <NuxtLink to="/resume/experience"><i class="bi bi-list-stars"></i>{{ ' ' }}Experience
        </NuxtLink>
        <NuxtLink to="/resume/language"><i class="bi bi-translate"></i>{{ ' ' }}Languages</NuxtLink>
        <NuxtLink to="/resume/certification"><i class="bi bi-patch-check"></i>{{ ' ' }}Certification
        </NuxtLink>
        <NuxtLink to="/resume/project"><i class="bi bi-blockquote-left"></i>{{ ' ' }}Projects
        </NuxtLink>
        <NuxtLink to="/resume/referee"><i class="bi bi-sliders2"></i>{{ ' ' }}Referees</NuxtLink>
        <NuxtLink to="/resume/preview"><i class="bi bi-eye-fill"></i>{{ ' ' }}Preview</NuxtLink>
    </div>

    <div class="main py-4 d-flex justify-contents-center">
        <slot />
    </div>
</template>

<script>

export default {
    data() {
        return {
            sidebarOpen: true,
        };
    },
    methods: {
        toggleSidebar() {
            this.sidebarOpen = !this.sidebarOpen;
        },
    },
};

</script>

<style>
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

    transition: width 0.3s;
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

.sidenav-open {
    width: 150px;
}

.sidenav-closed {
    width: 0;
    overflow: hidden;

}

.sidenav-closed~.main {
    margin-left: 0;
}

.main {
    margin-left: 150px;
    font-family: "Lato", sans-serif;
    /* font-family: "Times New Roman", Times, serif; */
    /* Same as the width of the sidenav */
    font-size: 14px;
    padding: 0px 0px;

    /* Adjust the margin for the open sidebar */
    transition: margin-left 0.3s;
}

.custom-navbar {
    background-color: rgba(11, 172, 236, 0.192);
    color: white;
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