import axios, { type AxiosResponse } from 'axios';
import { ref } from 'vue';

/**
 * ======================================================================
 * Author: Ronald Kimeli
 * Portfolio: [ronald-kimeli.github.io](https://ronald-kimeli.github.io)
 * ======================================================================
 */

export default defineNuxtPlugin((nuxtApp) => {
  const { public: { BASE_URL } } = useRuntimeConfig();

  /** 
   * State variables to track response, loading, and error
   */
  const response = ref<AxiosResponse<any> | null>(null);
  const loading = ref(false);
  const error = ref<null | unknown>(null);

  /** 
   * Create an Axios client with a base URL fetched from runtime config
   * We assert that `baseURL` will be a string
   */
  const axiosClient = axios.create({
    baseURL: BASE_URL as string, 
    headers: { 'Content-Type': 'application/json' },
  });

  /** 
   * Request interceptor
   * You can modify the request config (e.g., add headers)
   */
  axiosClient.interceptors.request.use((config) => {
    // Add any modifications before the request is sent
    return config;
  });

  /** 
   * Response interceptor
   * Handles the response and stores it, or catches errors
   */
  axiosClient.interceptors.response.use(
    (res) => {
      response.value = res;
      return res;
    },
    (err) => {
      error.value = err;
      return Promise.reject(err);
    }
  );

  /** 
   * Generic function to handle API requests
   * Supports: GET, POST, PUT, PATCH, DELETE
   */
  const makeRequest = async (
    method: 'get' | 'post' | 'put' | 'patch' | 'delete',
    url: string,
    data?: any,
    config = {}
  ) => {
    loading.value = true;
    error.value = null;
    try {
      const res = await axiosClient({
        method,
        url,
        data,
        ...config,
      });
      response.value = res;      
      return res;
    } catch (err) {
      error.value = err;
      throw err;
    } finally {
      loading.value = false;
    }
  };

  /** 
   * API methods for different request types
   */
  const get = (url: string, config = {}) => makeRequest('get', url, null, config);
  const post = (url: string, data: any, config = {}) => makeRequest('post', url, data, config);
  const put = (url: string, data: any, config = {}) => makeRequest('put', url, data, config);
  const patch = (url: string, data: any, config = {}) => makeRequest('patch', url, data, config);
  const del = (url: string, config = {}) => makeRequest('delete', url, null, config);

  /** 
   * Inject the `useAxios` functionality into the Nuxt app context
   * so it can be accessed globally
   */
  nuxtApp.provide('useAxios', { get, post, put, patch, del, response, loading, error });
});
