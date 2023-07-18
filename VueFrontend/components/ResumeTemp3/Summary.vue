<template>
   <div class="child summary">
      <div id="section-title">
        <h4><strong>Summary</strong></h4>
        <hr class="border border-black border-2 opacity-75">
      </div>
      <span class="summary description">
                Passionate web developer with more than 2 years of working experience
                working as a Full-Stack developer and a graduate of Computer Science.
                Always ready to learn and explore technology to provide the best
                services on both Back-end and Front-End technologies.
      </span>
    </div>
</template>

<script setup>

</script>

<style scoped>


.summary{
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