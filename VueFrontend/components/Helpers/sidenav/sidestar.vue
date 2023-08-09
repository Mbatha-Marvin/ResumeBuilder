<template>
    <div class="sidenav">
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#clients">Clients</a>
        <a href="#contact"><i class="bi bi-book"></i> {{ '' }}Education</a>
    </div>
    <div class="main">
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