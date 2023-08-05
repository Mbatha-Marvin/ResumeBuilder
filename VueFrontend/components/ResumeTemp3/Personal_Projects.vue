<template>
  <div class="child personal-projects">
    <div id="section-title">
      <h4><strong>Projects</strong></h4>
      <Helpers.Bold_hr />
    </div>
    
    <div v-for="(item, index) in projects" :key="index"  class="projects">
      <div class="iconic-section">
        <span><strong>Title :</strong><i> {{ item.project_name }}</i></span>
      </div>
      <div class="iconic-section">
        <span><strong>Skills :</strong> Comma separated skills, just at most 5</span>
      </div>
      <div class="iconic-section">
        <i class="bi bi-link-45deg mr-2"></i>
        <span><strong> {{ item.project_url }}</strong></span>
      </div>
      <div class="iconic-section">
        <span><strong>Description :</strong> {{ item.project_description_title }}.</span>
      </div>
      <Helpers.Dotted_hr v-if="index < projects.length - 1" />
    </div>
  </div>
</template>

<script setup>

const { projects } = defineProps(['projects'])

</script>

<style lang="scss" scoped>
.projects {
  text-align: left !important;
}

</style>