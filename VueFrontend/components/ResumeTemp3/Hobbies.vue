<template>
    <div class="child hobbies">
      <div id="section-title">
        <h4><strong>{{ hobbies.card_title }}</strong></h4>
        <Helpers.Bold_hr />
      </div>
      <div v-for="(item, index) in hobbies.hobbies" :key="index" class="row rowhobbies">
        <div class="col-md-6 iconic-section">
          <i class="bi bi-dot"></i><span>{{ item }}</span>
        </div>
      </div>
    </div>
</template>

<script setup>

const { hobbies } = defineProps(['hobbies']);

</script>

<style lang="scss" scoped>
.Hobbies {
    text-align: left !important;
}

</style>