import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useToastStore = defineStore('toast', () => {
  const message = ref('');

  const setMessage = (msg) => {
    message.value = msg;
  };

  const clearMessage = () => {
    message.value = '';
  };

  return { message, setMessage, clearMessage };
});
