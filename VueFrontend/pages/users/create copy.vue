<template>
  <div class="container mt-4">
    <div class="card shadow rounded">
      <div class="card-header">
        <h4 class="d-inline">Add User
          <NuxtLink to="/users" class="btn btn-outline-success float-end">Users</NuxtLink>
        </h4>
      </div>
      <div class="card-body">
        <form @submit.prevent="createUser">
          <div class="form-group">
            <label for="name">Name:</label>
            <input v-model="newUser.name" type="text" id="name" class="form-control"/>
            <span v-if="errors.name" class="text-danger">{{ errors.name }}</span>
          </div>
          <div class="form-group">
            <label for="email">Email:</label>
            <input v-model="newUser.email" type="email" id="email" class="form-control"/>
            <span v-if="errors.email" class="text-danger">{{ errors.email }}</span>
          </div>
          <div class="form-group">
            <label for="password">Password:</label>
            <input v-model="newUser.password" type="password" id="password" class="form-control"/>
            <span v-if="errors.password" class="text-danger">{{ errors.password }}</span>
          </div>
          <button type="submit" class="btn btn-primary mt-2">Submit</button>
        </form>
      </div>
    </div>
  </div>
</template>
  
<script>
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'CreateUser',
  setup() {
    const newUser = ref({ name: '', email: '', password: '' });
    const errors = ref({});

    const router = useRouter();

    const BASE_URL = "http://localhost:5000";

    const createUser = async () => {
      try {
        // Clear previous errors
        errors.value = {};
        const response = await useFetch(`${BASE_URL}/users`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(newUser.value),
        });

        if (response.status.value === 'success') {
          router.push('/users');
        } else if (response.status.value === 'error') {
          console.log(response);
          const errorData = await response;
          errors.value = errorData.errors;
        }
      } catch (error) {
        console.error('Error creating user:', error);
      }
    };
    
    return {
      newUser,
      errors,
      createUser,
    };
  },
});
</script>
  