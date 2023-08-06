<template>
   <div v-for="(item, index) in education" :key="index" class="enrolment">
        <div class="iconic-section">
          <span>Level : <strong>{{ item.education_level }}</strong></span>
        </div>
        <div class="iconic-section">
          <span>Course : <strong>{{ item.course_title }}</strong></span>
        </div>
        <div class="iconic-section">
          <span>Institution : <strong>{{ item.school_name }}</strong></span>
        </div>
        <div class="row">
          <div class="col-md-6 iconic-section">
            <span>Start Date : <strong>22/08/2016</strong></span>
          </div>
          <div class="col-md-6 iconic-section">
            <span>End Date : <strong>20/10/2020</strong></span>
          </div>
        </div>
        <Helpers.Dotted_hr v-if="index < education.length - 1" />
      </div>
</template>

<script setup>
        const { education } = defineProps(['education'])
</script>

<style lang="scss" scoped>

</style>