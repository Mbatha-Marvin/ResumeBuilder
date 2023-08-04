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
              <th>Name</th>
              <th>Password</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in users" :key="index">
              <td>{{ user.name }}</td>
              <td>{{ user.password }}</td>
              <td>
                <NuxtLink :to="`/users/${user.id}`" class="btn btn-sm btn-primary mx-2">Edit</NuxtLink>
                <button @click="deleteUser(user.id)" class="btn btn-sm btn-danger mx-2">Delete</button>
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
export default {
  name: "user",
  data() {
    return {
      users: [],
      newUser: {
        name: '',
        password: '',
      },
      isLoading: true
    };
  },
  mounted() {
    this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
      this.isLoading = true;
      try {
        const { data } = await useFetch('http://localhost:5000/users');
        const response = data.value;
        console.log(response);
        this.isLoading = false;
        this.users = await response;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    }
  },
};
</script>
