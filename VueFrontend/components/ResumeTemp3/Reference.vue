<template>
    <div class="child reference">
      <div id="section-title">
        <h4><strong>Reference</strong></h4>
        <hr class="border border-black border-2 opacity-75">
      </div>
      <div class="row referencerow">
      <div class="iconic-section">
        <span><strong>Name :</strong> Testing Jacobs</span>
      </div>
      <div class="iconic-section">
        <span><strong>Institution :</strong> Testing org centre</span>
      </div>
      <div class="iconic-section">
        <span><strong>Role :</strong> Web Dev</span>
      </div>
      <div class="iconic-section">
        <span><strong>Email :</strong>
        test@gmail.com</span>
      </div>
      <div class="iconic-section">
        <span><strong>Phone :</strong>
        254 798 298 834</span>
      </div>
      </div>
    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>


.reference {
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