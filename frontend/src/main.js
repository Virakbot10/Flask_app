import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';


// Configure Axios globally
axios.defaults.baseURL = 'http://localhost:5000';
axios.defaults.withCredentials = true;

// Token handling with Axios interceptor
axios.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

// Create and mount Vue app
const app = createApp(App);
app.use(router)
app.mount('#app');
