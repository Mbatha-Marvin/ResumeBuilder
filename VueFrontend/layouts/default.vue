<template>
    <div>
      <Navbar />
      <!-- <div class="container py-4 d-flex justify-contents-center"> -->
        <div :class="containerClasses">
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
    computed: {
    containerClasses() {
      return {
        container: true,
        'py-4': true,
        'd-flex': true,
        'justify-content-center': true,
        'justify-content-sm-between': true  // Change this class based on your desired behavior
      };
    }
  }
  };
  </script>
  
  <style scoped>

  </style>
  