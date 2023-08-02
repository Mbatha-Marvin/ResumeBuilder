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
            <input v-model="newUser.name" type="text" id="name" class="form-control" required />
          </div>
          <div class="form-group">
            <label for="email">Email:</label>
            <input v-model="newUser.email" type="email" id="email" class="form-control" required />
          </div>
          <div class="form-group">
            <label for="password">Password:</label>
            <input v-model="newUser.password" type="password" id="password" class="form-control" required />
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

    const router = useRouter();

    const BASE_URL = "http://localhost:5000";

    const createUser = async () => {
      try {
        await useFetch(`${BASE_URL}/users`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(newUser.value),
        });
        router.push('/users');
      } catch (error) {
        console.error('Error creating user:', error);
      }
    };

    return {
      newUser,
      createUser,
    };
  },
});
</script>
  