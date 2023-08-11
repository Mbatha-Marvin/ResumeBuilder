<template>
  <div>
    <form @submit.prevent="submitForm">
      <div>
        <label for="username">Username:</label>
        <input id="username" v-model="myData.username" placeholder="Enter username" />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="myData.password" placeholder="Enter password" />
      </div>
      <div>
        <label for="description">Description:</label>
        <input id="description" v-model="newDescription" placeholder="Enter a description" />
        <button type="button" @click="addDescription">Add Description</button>
      </div>
      <div v-for="(description, index) in myData.descriptions" :key="index" class="description-entry">
        {{ description }}
        <button type="button" @click="removeDescription(index)">Delete</button>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

// Data
const myData = ref({ username: '', password: '', descriptions: [] });
const newDescription = ref('');

// Methods
const addDescription = () => {
  if (newDescription.value.trim() !== '') {
    if (myData.descriptions.length < 5) {
      myData.descriptions.push(newDescription.value);
    } else {
      // Implement logic to display an error or warning when the limit is reached
    }
    
    newDescription.value = '';
  }
};

const removeDescription = (index) => {
  myData.descriptions.splice(index, 1);
};

const submitForm = async () => {
  // Send data to the server to create or update a product
  try {
    const response = await axios.post('/products', myData.value);
    console.log('Product created/updated:', response.data);
    // Reset form fields
    myData.username = '';
    myData.password = '';
    myData.descriptions.length = 0;
  } catch (error) {
    console.error('Error creating/updating product:', error);
  }
};

// Fetch initial data if needed
onMounted(async () => {
  try {
    const response = await axios.get('/products');
    console.log('Initial data fetched:', response.data);
    // Handle the fetched data as needed
  } catch (error) {
    console.error('Error fetching initial data:', error);
  }
});
</script>
