import axios from 'axios';

export default defineNuxtPlugin(() => {
  const { public: { BASE_URL } } = useRuntimeConfig();

  const instance = axios.create({
    baseURL: `${BASE_URL}`, 
    // timeout: 1000,
    headers: { 'Content-Type': 'application/json' },
  });
  return {
    provide: {
      axios: instance
    }
  }
});

