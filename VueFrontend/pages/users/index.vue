<template>
  <div class="container mt-4">
    <div class="card shadow rounded">
      <div class="card-header">
        <h4 class="d-inline">User List
          <NuxtLink to="/users/create" class="btn btn-outline-success float-end">Create User</NuxtLink>
        </h4>
      </div>
      <div class="card-body">
        <div class="table-responsive-md table-responsive-sm table-responsive-lg table-responsive-xl table-responsive-xxl">
          <table class="table table-striped table-bordered rounded">
            <thead>
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Password</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(user, index) in users" :key="index">
                <td>{{ user.user_id }}</td>
                <td>{{ user.name }}</td>
                <td>{{ user.email }}</td>
                <td>
                  <div class="btn-group" role="group" aria-label="Third group">
                    <NuxtLink :to="`/users/${user.user_id}`" class="btn btn-sm btn-primary mx-2">Edit</NuxtLink>
                    <button @click="deleteUser(user.user_id)" class="btn btn-sm btn-danger mx-2">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';


export default defineComponent({
  name: 'UserList',
  setup() {
    const users = ref({ user_id: '', name: '', email: '' });

    const BASE_URL = "http://localhost:5000";

    const fetchUsers = async () => {
      try {
        const { data } = await useFetch(`${BASE_URL}/users`);
        const response = data.value;
        users.value = await response;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    };

    const deleteUser = async (userId) => {
      try {
        await useFetch(`${BASE_URL}/users/${userId}`, { method: 'DELETE' });
        console.log(userId);
        await fetchUsers();
      } catch (error) {
        console.error('Error deleting user:', error);
      }
    };

    onMounted(() => {
      fetchUsers();
    });

    return {
      users,
      deleteUser,
    };
  },
});
</script>
