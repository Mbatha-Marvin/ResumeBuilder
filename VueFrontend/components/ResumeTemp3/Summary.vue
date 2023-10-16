<template>
   <div class="child summary">
      <div id="section-title">
        <h4><strong>{{ summary.card_title }}</strong></h4>
        <Helpers.Bold_hr />
      </div>
      <span class="summary description">
             {{ summary.brief_description }}
      </span>
    </div>
</template>

<script setup>
const { summary } = defineProps(['summary'])

</script>

<style scoped>
.summary{
    text-align: left !important;
}

</style>