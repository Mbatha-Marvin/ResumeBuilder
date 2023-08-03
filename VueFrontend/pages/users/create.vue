<template>
  <div class="container mt-4">
    <div class="card shadow rounded">
      <div class="card-header">
        <h4 class="d-inline">Add User
          <NuxtLink to="/users" class="btn btn-outline-success float-end">Users</NuxtLink>
        </h4>
      </div>
      <div class="card-body">

        <form @submit.prevent="submitForm" class="needs-validation" novalidate>
          <div class="form-group">
            <label for="name" class="form-label">Name:</label>
            <input v-model="newUser.name" type="text" id="name" class="form-control" required />
            <span class="invalid-feedback">Name is required</span>
          </div>
          <div class="form-group">
            <label for="email" class="form-label">Email:</label>
            <input v-model="newUser.email" type="email" id="email" class="form-control" required />
            <span class="invalid-feedback">Email is required</span>
            <span v-if="errorMessage" class="error-message">{{ errorMessage }}</span>
          </div>
          <div class="form-group">
            <label for="password" class="form-label">Password:</label>
            <input v-model="newUser.password" type="password" id="password" class="form-control" required />
            <span class="invalid-feedback">Password is required</span>
          </div>
          <button @click="toggleAlert" type="submit" class="btn btn-primary mt-2">Submit</button>
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
    const errorMessage = ref('');

    const router = useRouter();

    const BASE_URL = "http://localhost:5000";

    const createUser = async () => {
      const form = document.querySelector('.needs-validation');
      if (form.checkValidity()) {

        const response = await useFetch(`${BASE_URL}/users`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(newUser.value),
        });

        if (response.status.value === "error") {
          errorMessage.value = 'Email already taken';
        }
        // console.log('Form submission successful');
        // router.push('/users');
      } else {
        form.classList.add('was-validated');
      };
    };

    onMounted(() => {
      const forms = document.querySelectorAll('.needs-validation');

      Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
          event.preventDefault();
          event.stopPropagation();

          if (!form.checkValidity()) {
            form.classList.add('was-validated');
          } else {
            createUser();
          }
        }, false);
      });
    });

    return {
      newUser,
      createUser,
    };
  },
});
</script>
