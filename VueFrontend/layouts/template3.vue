<template>   
<div class="container mains">
  <Navbar />
  <div class="row">
    <slot /> 
  </div>
</div>

</template>
  
<script setup>

</script>

<style scoped>
.mains {
    background: #ffffff !important;
    /* margin: 20px !important;
    padding: 20px !important; */
}
</style>
  