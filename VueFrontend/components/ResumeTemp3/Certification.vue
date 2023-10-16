<template>
 <div class="child certification">
      <div id="section-title">
        <h4><strong>{{ certification.card_title }}</strong></h4>
        <Helpers.Bold_hr />
      </div>
      <div v-for="(item, index) in certification.certification_details" :key="index" class="experience">
      <div class="certified">
        <div class="iconic-section">
          <span><strong>Certified On :</strong> {{ item.certified_on }}</span>
        </div>
        <div class="iconic-section">
          <span><strong>School Name :</strong> {{ item.school_name }}</span>
        </div>
        <div class="iconic-section">
          <span><strong>School Type :</strong> {{ item.school_type }}</span>
        </div>
        <div class="row">
          <div class="col-md-6 iconic-section">
            <span><strong>Start Date:</strong> {{ item.start_date }}</span>
          </div>
          <div class="col-md-6 iconic-section">
            <span><strong>End Date:</strong> {{ item.end_date }}</span>
          </div>
        </div>
        <Helpers.Dotted_hr v-if="index < certification.certification_details.length - 1" />
      </div>
    </div>
    </div>
</template>

<script setup>
const { certification } = defineProps(['certification']);

</script>

<style lang="scss" scoped>
.certification {
    text-align: left !important;
}

</style>