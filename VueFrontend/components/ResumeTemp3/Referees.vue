<template>
    <div class="child reference">
      <div id="section-title">
        <h4><strong>{{ referee.card_title }}</strong></h4>
        <Helpers.Bold_hr />
      </div>
      <div v-for="(item, index) in referee.referee_details" :key="index" class="row referencerow">
      <div class="iconic-section">
        <span><strong>Name :</strong> {{ item.full_name }}</span>
      </div>
      <div class="iconic-section">
        <span><strong>Institution :</strong> {{ item.company_name }}</span>
      </div>
      <div class="iconic-section">
        <span><strong>Role :</strong> {{ item.occupation }}</span>
      </div>
      <div class="iconic-section">
        <span><strong>Email :</strong>
        {{ item.email }}</span>
      </div>
      <div class="iconic-section">
        <span><strong>Phone :</strong>
         {{ item.phone_number }}</span>
      </div>
      
      <Helpers.Dotted_hr v-if="index < referee.referee_details.length - 1" />
      </div>
    </div>
</template>

<script setup>

const { referee } = defineProps(['referee'])
</script>

<style lang="scss" scoped>
.reference {
    text-align: left !important;
}

</style>