<template>
    <div class="container">
        <div class="card mb-2">
            <div class="card-body rounded">
                <h4 class="text-center text-uppercase bold">Login</h4>
            </div>
        </div>
        <div class="card shadow rounded">
            <div class="card-body">
                <form @submit.prevent="loginUser" class="needs-validation" novalidate>
                    <div class="form-group mb-2">
                        <label for="email" class="form-label">Email</label>
                        <input v-model="loggedUser.email" type="email" id="email" class="form-control"
                            placeholder="Enter Email" required />
                        <span class="invalid-feedback">Email is required</span>
                        <span v-if="errorMessage" class="form-text error-text">{{ errorMessage }}</span>
                    </div>
                    <div class="form-group mb-2">
                        <label for="password" class="form-label">Password</label>
                        <input v-model="loggedUser.password" type="password" id="password" class="form-control"
                            placeholder="Enter Password" required />
                        <span class="invalid-feedback">Password is required</span>
                    </div>
                    <div class="d-inline align-baseline mt-2">
                        <button type="submit" class="btn btn-success mt-2">Login</button>
                        <NuxtLink to="/auth/register" class="float-end text-center mt-2">New user? register</NuxtLink>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
  
<script>
import { defineComponent, ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export default defineComponent({
    name: 'EditUser',
    setup() {
        const loggedUser = ref({ email: '', password: '' });
        const errorMessage = ref('');
        const isError = ref('form-control');

        const route = useRoute();

        const router = useRouter();

        const BASE_URL = "http://localhost:5000";

        const loginUser = async () => {
            errorMessage.value = '';
            const form = document.querySelector('.needs-validation');
            if (form.checkValidity()) {
                errorMessage.value = '';
                const response = await useFetch(`${BASE_URL}/users/${route.params.id}`);
                loggedUser.value = await response;

                if (response.status.value === "error") {
                    errorMessage.value = 'Email already taken';
                    isError.value = 'form-control border-danger';
                } else {
                    console.log('Logged in successful');
                    errorMessage.value = '';
                    isError.value = 'form-control';
                    router.push('/resume/dashboard');
                }
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
                        loginUser();
                    }
                }, false);
            });
        });

        if (errorMessage) {
            return {
                loggedUser,
                errorMessage,
                isError
            }
        } else {
            return {
                loggedUser,
                loginUser,
            };
        }
    },
});
</script>
  