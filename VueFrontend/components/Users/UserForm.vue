<template>
    <form @submit.prevent="addUser">
      <div>
        <label for="name">Name:</label>
        <input v-model="newUser.name" type="text" id="name" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input v-model="newUser.email" type="email" id="email" required />
      </div>
      <button type="submit">Add User</button>
    </form>
  </template>
  
  <script>
  import { mapActions } from 'vuex';
  
  export default {
    data() {
      return {
        newUser: {
          name: '',
          email: '',
        },
      };
    },
    methods: {
      ...mapActions('users', ['addUser']),
    },
  };
  </script>
  