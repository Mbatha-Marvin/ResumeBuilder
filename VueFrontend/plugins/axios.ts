import axios from 'axios';

export default defineNuxtPlugin( () => {
    const instance = axios.create({
        baseURL: 'http://localhost:5000/api/v1',
        // timeout: 1000,
        headers: { 'Content-Type': 'application/json' },
      });
      return {
        provide: {
            axios: instance
        }
      }
  })
  
  