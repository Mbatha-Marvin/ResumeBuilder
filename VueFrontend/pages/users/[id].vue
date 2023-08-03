<template>
    <div class="container mt-4">
        <div class="card shadow rounded">
            <div class="card-header">
                <h4 class="d-inline">Update User
                    <NuxtLink to="/users" class="btn btn-outline-danger float-end">Back</NuxtLink>
                </h4>
            </div>
            <div class="card-body">
                <form @submit.prevent="updateUser">
                    <div class="form-group">
                        <label for="user_id">Id:</label>
                        <input v-model="editedUser.user_id" type="text" id="user_id" class="form-control" readonly />
                    </div>
                    <div class="form-group">
                        <label for="name">Name:</label>
                        <input v-model="editedUser.name" type="text" id="name" class="form-control" required />
                    </div>
                    <div class="form-group">
                        <label for="email">Email:</label>
                        <input v-model="editedUser.email" type="email" id="email" class="form-control" required />
                    </div>
                    <div class="form-group">
                        <label for="password">Password:</label>
                        <input v-model="editedUser.password" type="password" id="password" class="form-control" required />
                    </div>
                    <button type="submit" class="btn btn-primary mt-2">Update</button>
                </form>
            </div>
        </div>
    </div>
</template>
  
<script >
import { defineComponent, ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export default defineComponent({
    name: 'EditUser',
    setup() {
        const editedUser = ref({ user_id: '', name: '', email: '', password: '' });

        const route = useRoute();
        const router = useRouter();

        const BASE_URL = "http://localhost:5000";

        const fetchUser = async () => {
            try {
                const { data } = await useFetch(`${BASE_URL}/users/${route.params.id}`);
                const response = data.value;
                editedUser.value = await response;
            } catch (error) {
                console.error('Error fetching user:', error);
            }
        };

        const updateUser = async () => {
            try {
                await useFetch(`${BASE_URL}/users/${route.params.id}`, {
                    method: 'PATCH',
                    body: JSON.stringify(editedUser.value),
                });
                router.push('/users');
            } catch (error) {
                console.error('Error updating user:', error);
            }
        };

        onMounted(() => {
            fetchUser();
        });

        return {
            editedUser,
            updateUser,
        };
    },
});
</script>
  