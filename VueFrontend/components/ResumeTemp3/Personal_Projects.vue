<template>
  <div class="child personal-projects">
    <div id="section-title">
      <h4><strong>Personal Projects</strong></h4>
      <hr class="border border-black border-2 opacity-75">
    </div>
    <div class="projects">
      <div class="company-title">
        <span><strong>Title :</strong> Leave management app</span>
      </div>
      <div class="iconic-section">
        <span><strong>Skills :</strong> React js && Laravel</span>
      </div>
      <div class="iconic-section">
        <i class="bi bi-link-45deg mr-2"></i>
        <span><strong>https://leave-managent-system.great-site.net</strong></span>
      </div>
      <div class="iconic-section">
        <span><strong>Description :</strong> Online leave management system</span>
      </div>
    </div>
    <Helpers.Dotted_hr />
    <div class="projects">
      <div class="company-title">
        <span><strong>Title :</strong> Leave management app</span>
      </div>
      <div class="iconic-section">
        <span><strong>Skills :</strong> React js && Laravel</span>
      </div>
      <div class="iconic-section">
        <i class="bi bi-link-45deg mr-2"></i>
        <span><strong>https://leave-managent-system.great-site.net</strong></span>
      </div>
      <div class="iconic-section">
        <span><strong>Description :</strong> Online leave management system</span>
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>
.projects {
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