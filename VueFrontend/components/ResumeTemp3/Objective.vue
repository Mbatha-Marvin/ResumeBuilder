<template>
   <div class="child objective">
      <div id="section-title">
        <!-- <h4><strong>{{ objective.card_title }}</strong></h4> -->
        <h4><strong>{{ `Objective` }}</strong></h4>

        <Helpers.Bold_hr />
      </div>
      <span class="objective description">
             {{ objective.brief_description }}
      </span>
    </div>
</template>

<script setup>
const { objective } = defineProps(['objective'])

</script>

<style scoped>
.objective{
    text-align: left !important;
}

</style>