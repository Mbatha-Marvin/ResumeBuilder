<template>
    <div class="child programming">
      <div id="section-title">
        <h4><strong>Programming Languages</strong></h4>
        <hr class="border border-black border-2 opacity-75">
      </div>
      
      <div class="row rowprogram">
      <div class="iconic-section">
        <span><strong>JavaScript :</strong> Expert</span>
      </div>
      <div class="iconic-section">
        <span><strong>Python :</strong> Intermediate</span>
      </div>
      <div class="iconic-section">
        <span><strong>PHP :</strong> Expert</span>
      </div>
      <div class="iconic-section">
        <span><strong>Golang :</strong> Beginner</span>
      </div>
      </div>
    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>


.programming {
    text-align: left !important;
}



.parent{
    columns: 2;
    gap: 10px;
    padding: 5px;
    margin: 0 auto;
  }
  
  .child{
    padding: 10px;
    background-color: white;
    display: inline-block;
    width: 100%;  
    margin-bottom: 5px;
  }
</style>