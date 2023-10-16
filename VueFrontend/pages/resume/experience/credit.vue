<template>
  <div>
    <div v-for="(description, descriptionIndex) in experience.job_descriptions" :key="descriptionIndex" class="description-entry">
      <!-- <input v-model="description" /> -->
      <button type="button" @click="removeDescription(descriptionIndex)">Delete</button>
    </div>
    
    <div>
      <input v-model="newDescription" />
      <button type="button" @click="addDescription">Add</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';


const experience = ref({
  job_descriptions: ['Description 1', 'Description 2', 'Description 3']
});

const newDescription = ref('');

const removeDescription = (descriptionIndex) => {
  experience.value.job_descriptions.splice(descriptionIndex, 1);
};

const addDescription = () => {
  if (newDescription.value.trim() !== '') {
    experience.value.job_descriptions.push(newDescription.value);
    newDescription.value = '';
  }
};
</script>
