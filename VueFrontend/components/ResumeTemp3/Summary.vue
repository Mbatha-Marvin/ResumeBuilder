<template>
   <div class="child summary">
      <div id="section-title">
        <h4><strong>Summary</strong></h4>
        <Helpers.Bold_hr />
      </div>
      <span class="summary description">
             {{ resume.user_contact_details[0].user_summary }}
      </span>
    </div>
</template>

<script setup>
const { resume } = defineProps(['resume'])

</script>

<style scoped>
.summary{
    text-align: left !important;
}

</style>