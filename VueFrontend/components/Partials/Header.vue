<template>
  <div class="row py-4 px-2">
    <div class="col-xl-12 col-lg-12 col-md-12">
      <div class="card mb-2">
        <div class="card-body rounded">
          <!-- Bind the title prop to the h4 tag -->
          <h4 class="text-center text-uppercase bold">{{ title }}</h4>
        </div>
      </div>
      <div class="card mb-2">
        <div class="card-content collapse show">
          <div class="card-body card-dashboard">
            <slot />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  title: {
    type: String,
    required: true
  }
});

const emits = defineEmits();
</script>

<style scoped></style>