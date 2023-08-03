<template>
    <div>
      <Navbar />
      <div class="container py-4 d-flex justify-contents-center">
        <slot />
      </div>
      <br />
      <Footer />
    </div>
  </template>
  
  <script>
  import Navbar from "../components/Includes/Navbar";
  import Footer from "../components/Includes/Footer.vue";
  
  export default {
    components: {
      Navbar,
      Footer,
    },
  };
  </script>
  
  <style scoped>

  </style>
  