<template>
  <div>
    <h1>User Registration and Descriptions</h1>
    <credit />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import credit from './credit.vue';

export default defineComponent({
  components: {
    credit,
  },
});
</script>
