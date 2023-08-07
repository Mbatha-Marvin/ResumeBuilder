<template>
  <div class="container">
    <div class="card mb-2">
      <div class="card-body">
        <h4 class="text-center text-uppercase bold">Register</h4>
      </div>
    </div>
    <div class="card shadow rounded">
      <div class="card-body">
        <form @submit.prevent="submitForm" class="needs-validation" novalidate>
          <div class="form-group">
            <label for="name" class="form-label">Username</label>
            <input v-model="newUser.name" type="text" id="name" class="form-control" placeholder="Enter Username"
              required />
            <span class="invalid-feedback">Name is required</span>
          </div>
          <div class="form-group">
            <label for="email" class="form-label">Email</label>
            <input v-model="newUser.email" type="email" id="email" :class="isError" placeholder="Enter Email" required />
            <span class="invalid-feedback">Email is required</span>
            <span v-if="errorMessage" class="form-text error-text">{{ errorMessage }}</span>
          </div>
          <div class="form-group">
            <label for="password" class="form-label">Password</label>
            <input v-model="newUser.password" type="password" id="password" class="form-control"
              placeholder="Enter Password" required />
            <span class="invalid-feedback">Password is required</span>
          </div>
          <div class="d-inline mt-2 align-baseline mt-2">
            <button type="submit" class="btn btn-success mt-2">Register</button>
            <NuxtLink to="/auth/login" class="float-end text-center mt-2">Already registered? login</NuxtLink>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
  
<script>
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import Bold_hr from '../../components/Helpers/Bold_hr.vue';

export default defineComponent({
  name: 'CreateUser',
  setup() {

    const newUser = ref({ name: '', email: '', password: '' });
    const errorMessage = ref('');
    const isError = ref('form-control');

    const router = useRouter();

    const BASE_URL = "http://localhost:5000";

    const createUser = async () => {
      errorMessage.value = '';
      const form = document.querySelector('.needs-validation');
      if (form.checkValidity()) {
        errorMessage.value = '';
        await axios({
          method: 'post',
          url: `${BASE_URL}/users`,
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify(newUser.value),
        })
          .then(function (response) {
            console.log('Registration successful');
            errorMessage.value = '';
            isError.value = 'form-control';
            router.push('/users');
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
            errorMessage.value = error.response.data.detail;
            isError.value = 'form-control border-danger';
          });
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

    if (errorMessage) {
      return {
        newUser,
        errorMessage,
        isError
      }
    } else {
      return {
        newUser,
        createUser,
      };
    }

  },
});
</script>

<style scoped>
.form-control .border-danger {
  border: 2px solid #921f1f !important;
  background-color: #921f1f !important;
  content: "!";
  position: absolute;
  top: 50%;
  right: 10px;
  /* Adjust the spacing as needed */
  transform: translateY(-50%);
  color: red;
  font-weight: bold;
}

.error {
  border: 1px solid red;
}

.error-text {
  color: red;
  margin-top: 5px;
}
</style>











