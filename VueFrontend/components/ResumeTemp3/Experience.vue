<template>
  <div class="child work-experience">
    <div id="section-title">
      <h4><strong>Experience</strong></h4>
      <Helpers.Bold_hr />
    </div>

    <div v-for="(item, index) in experience" :key="index" class="experience">
      <div id="experience-title">
        <h5><strong>{{ item.job_title }} </strong></h5>
      </div>
      <div class="company-title">
        <img class="masterclass" src="/assets/img/masterclass.jpeg" alt="logo" />
        <span><strong>{{ item.company_name }}</strong></span>
      </div>
      <div class="iconic-section">
        <i class="bi bi-link-45deg mr-2"></i>
        <span><strong>{{ item.company_url }}</strong></span>
      </div>
      <div class="iconic-section">
        <i class="bi bi-geo-alt-fill"></i>
        <span><strong>{{ item.location }}</strong></span>
      </div>
      <div class="row rowdates">
        <div class="col-md-6 iconic-section">
          <span>Start Date: <strong>{{ item.start_date }}</strong></span>
        </div>
        <div class="col-md-6 iconic-section">
          <span>End Date: <strong>{{ item.end_date }}</strong></span>
        </div>
      </div>
      <div class="achievements mt-2">
        <div class="achivementtitle">
          <h6><strong>Achievements</strong></h6>
        </div>

        <div v-for="(description, index) in item.job_descriptions" :key="index">
          <div class="iconic-section">
            <i class="bi bi-dot"></i><span>{{ description }}</span>
          </div>
        </div>
      </div>
      <Helpers.Dotted_hr v-if="index < experience.length - 1" />

    </div>
  </div>
</template>

<script setup>
const { experience } = defineProps(['experience'])
</script>

<style scoped>
.experience {
  text-align: left !important;
}

#experience-title {
  text-align: start !important;
  text-decoration: none !important;
  width: auto !important;
}

img {
  background-color: inherit !important;
  height: 20px !important;
  width: 20px !important;
  margin-right: 4px !important;
}

.company-title {
  background-color: inherit !important;
  size: 20px !important;
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