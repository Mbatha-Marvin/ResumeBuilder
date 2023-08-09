<template>
  <div class="child personal-projects">
    <div id="section-title">
      <h4><strong>{{ projects.card_title }}</strong></h4>
      <Helpers.Bold_hr />
    </div>
    
    <div v-for="(item, index) in projects.project_details" :key="index"  class="projects">
      <div class="iconic-section">
        <span><strong>Title :</strong><i> {{ item.project_title }}</i></span>
      </div>
      <div class="iconic-section">
        <i class="bi bi-link-45deg mr-2"></i>
        <span><strong> {{ item.project_url }}</strong></span>
      </div>
      <div class="iconic-section">
        <span><strong>Description :</strong> {{ item.project_description_title }}.</span>
      </div>
      <div v-for="(description, index) in item.project_description_list" :key="index">
          <div class="iconic-section">
            <i class="bi bi-dot"></i><span>{{ description }}</span>
          </div>
      </div>
      <Helpers.Dotted_hr v-if="index < projects.project_details.length - 1" />
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