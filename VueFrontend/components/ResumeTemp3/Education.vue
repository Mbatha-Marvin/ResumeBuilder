<template>
  <div class="child education">
    <div id="section-title">
      <h4><strong>Education</strong></h4>
      <Helpers.Bold_hr />
    </div>

    <div v-for="(item, index) in education" :key="index" class="enrolment">
      <div class="iconic-section">
        <span><strong>Level : </strong> {{ item.education_level }}</span>
      </div>
      <div class="iconic-section">
        <span><strong>Course : </strong> {{ item.course_title }}</span>
      </div>
      <div class="iconic-section">
        <span><strong>Institution : </strong> {{ item.school_name }}</span>
      </div>
      <div class="row">
        <div class="col-md-6 iconic-section">
          <span><strong>Start Date:</strong> {{ item.start_date }}</span>
        </div>
        <div class="col-md-6 iconic-section">
          <span><strong>End Date:</strong> {{ item.finish_date }}</span>
        </div>
      </div>
      <Helpers.Dotted_hr v-if="index < education.length - 1" />
    </div>
  </div>
</template>

<script setup>
const { education } = defineProps(['education'])
</script>

<style lang="scss" scoped>
.education {
  text-align: left !important;
}
</style>