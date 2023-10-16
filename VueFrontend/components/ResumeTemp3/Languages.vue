<template>
  <div class="child languages">
    <div id="section-title">
      <h4><strong>{{ languages.card_title }}</strong></h4>
      <Helpers.Bold_hr />
    </div>
    <div v-for="(item, index) in languages.language_details" :key="index" class="language">
      <div class="iconic-section">
        <span><strong>{{ item.language_name }} :</strong> {{ item.profeciency_level }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>

const { languages } = defineProps(['languages'])

</script>

<style lang="scss" scoped>
.languages {
  text-align: left !important;
}

</style>