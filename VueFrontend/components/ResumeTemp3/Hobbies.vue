<template>
    <div class="child hobbies">
      <div id="section-title">
        <h4><strong>Hobbies</strong></h4>
        <hr class="border border-black border-2 opacity-75">
      </div>
      <div class="row rowhobbies">
        <div class="col-md-6 iconic-section">
          <i class="bi bi-dot"></i><span>Visiting the sick</span>
        </div>
        <div class="col-md-6 iconic-section">
          <i class="bi bi-dot"></i><span>Exploring new technology</span>
        </div>
        <div class="col-md-6 iconic-section">
          <i class="bi bi-dot"></i><span>Participating for community e.g. open
          source contribution</span>
        </div>
        <div class="col-md-6 iconic-section">
          <i class="bi bi-dot"></i><span>Gym for body fitness</span>
        </div>
      </div>
    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>


.Hobbies {
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