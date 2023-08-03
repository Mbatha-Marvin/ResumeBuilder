<template>
    <div>
      <h1>Users</h1>
      <ul>
        <li v-for="user in users" :key="user.id">
          {{ user.name }} - {{ user.password }}
          <button @click="deleteUser(user.id)">Delete</button>
        </li>
      </ul>
      <form @submit.prevent="addUser">
        <div>
          <label for="name">Name:</label>
          <input v-model="newUser.name" type="text" id="name" required />
        </div>
        <div>
          <label for="password">password:</label>
          <input v-model="newUser.password" type="password" id="password" required />
        </div>
        <button type="submit">Add User</button>
      </form>
    </div>
  </template>
  
  <script>
  
 const resumeBaseUrl = "http://localhost:5000";
  
  export default {
    data() {
      return {
        users: [],
        newUser: {
          name: '',
          password: '',
        },
      };
    },
    async users() {
      await this.fetchUsers();
    },
    methods: {
      async fetchUsers() {
        try {
          const response = await $fetch(`${resumeBaseUrl}/users`);
          this.users = await response.json();
        } catch (error) {
          console.error('Error fetching users:', error);
        }
      },
      async addUser() {
        try {
          const response = await $fetch(`${resumeBaseUrl}/users`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.newUser),
          });
          const newUser = await response.json();
          this.users.push(newUser);
          this.newUser = { name: '', password: '' };
        } catch (error) {
          console.error('Error adding user:', error);
        }
      },
      async deleteUser(userId) {
        try {
          await $fetch(`${resumeBaseUrl}/users/${userId}`, {
            method: 'DELETE',
          });
          this.users = this.users.filter((user) => user.id !== userId);
        } catch (error) {
          console.error('Error deleting user:', error);
        }
      },
    },
  };
  </script>
  