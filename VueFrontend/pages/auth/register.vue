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
            <label for="email" class="form-label">Email:</label>
            <input v-model="newUser.email" type="email" id="email" :class="isErrorEmail" placeholder="Enter Email"
              required />
            <span class="invalid-feedback">Email is required</span>
            <small v-if="errorMessageEmail" class="form-text error-text">{{ errorMessageEmail }}</small>
          </div>
          <div class="form-group">
            <label for="phone_number" class="form-label">Phone Number:</label>
            <input v-model="newUser.phone_number" type="tel" id="phone_number" :class="isErrorPhone" name="phone_number"
              class="form-control" placeholder="Enter Phone Number" pattern="[+]{1}[0-9]{3}[0-9]{3}[0-9]{6}" required>
            <span class="invalid-feedback">A valid Phone Number is required</span>
            <small v-if="errorMessagePhone" class="form-text error-text">{{ errorMessagePhone }}</small>
            <small v-show="!errorMessagePhone">Format is: +254722122333</small>
          </div>
          <div class="form-group">
            <label for="password" class="form-label">Password:</label>
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

export default defineComponent({
  name: 'CreateUser',
  setup() {
    const axios = useNuxtApp().$axios;
    const newUser = ref({ phone_number: '', email: '', password: '' });
    const errorMessageEmail = ref('');
    const errorMessagePhone = ref('');
    const isErrorPhone = ref('form-control');
    const isErrorEmail = ref('form-control');
    const router = useRouter();

    const createUser = async () => {
      const form = document.querySelector('.needs-validation');
      errorMessageEmail.value = '';
            errorMessagePhone.value = '';
            isErrorPhone.value = 'form-control';
            isErrorEmail.value = 'form-control';
      if (form.checkValidity()) {
        await axios({
          method: 'post',
          url: '/user',
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify(newUser.value),
        })
          .then(function (response) {
            console.log('Registration successful');
            errorMessageEmail.value = '';
            errorMessagePhone.value = '';
            isErrorPhone.value = 'form-control';
            isErrorEmail.value = 'form-control';
            router.push('/auth/login');
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
            if (error.response.data.detail['Email Exists']) {
              errorMessageEmail.value = 'Email Already Exists';
              isErrorPhone.value = 'form-control';
              isErrorEmail.value = 'form-control border-danger';
            } else if (error.response.data.detail['Phone Number Exists']) {
              errorMessagePhone.value = 'Phone Number Already Exists';
              isErrorPhone.value = 'form-control border-danger';
              isErrorEmail.value = 'form-control';
            }
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
            errorMessageEmail.value = '';
            errorMessagePhone.value = '';
            isErrorPhone.value = 'form-control';
            isErrorEmail.value = 'form-control';
          } else {
            createUser();
          }
        }, false);
      });
    });

    if (errorMessagePhone || errorMessageEmail) {
      return {
        newUser,
        errorMessagePhone,
        errorMessageEmail,
        isErrorEmail,
        isErrorPhone
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











