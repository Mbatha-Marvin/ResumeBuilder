<template>
    <div class="child skills">
      <div id="section-title">
        <h4><strong>Skills</strong></h4>
        <Helpers.Bold_hr />
      </div>
      <div class="row skillsrow">       
        <div v-for="(skill, index) in skills" :key="index" class="col-md-6 iconic-section">
          <i class="bi bi-dot"></i><span>{{ skill }}</span>
        </div>
      </div>
    </div>
</template>

<script setup>

const { skills } = defineProps(['skills'])

</script>

<style scoped>

.skills {
    text-align: left !important;
}

  
</style>