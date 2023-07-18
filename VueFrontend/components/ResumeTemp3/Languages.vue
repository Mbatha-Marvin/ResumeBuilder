<template>
  <div class="child languages">
    <div   id="section-title">
      <h4><strong>Languages</strong></h4>
      <hr class="border border-black border-2 opacity-75">
    </div>
    <div class="language">
      <div class="iconic-section">
        <span><strong>English :</strong> Profesional</span>
      </div>
      <div class="iconic-section">
        <span><strong>Kiswahili :</strong> Native</span>
      </div>
      <div class="iconic-section">
        <span><strong>French :</strong> Beginner</span>
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>


.languages {
  text-align: left !important;
}



.parent {
  columns: 2;
  gap: 10px;
  padding: 5px;
  margin: 0 auto;
}

.child {
  padding: 10px;
  background-color: white;
  display: inline-block;
  width: 100%;
  margin-bottom: 5px;
}
</style>