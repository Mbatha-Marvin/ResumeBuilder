import Vue3Toastify, { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import { useToastStore } from '@/stores/toastStore';

export default defineNuxtPlugin((nuxtApp: any) => {
  nuxtApp.vueApp.use(Vue3Toastify, { autoClose: 1000 });

  const showToast = (msg:string) => {
    const toastStore = useToastStore();
    toast.success(msg, {
      position: toast.POSITION.TOP_RIGHT,
      autoClose: 1000,
    });

    toastStore.setMessage(msg);
    toastStore.clearMessage();

  };

  return {
    provide: {
      showToast,
    },
  };
});
