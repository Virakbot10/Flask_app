import Vue from 'vue';
import App from '../App.vue';
import axios from 'axios';

Vue.config.productionTip = false;

// Set up Axios to interact with Flask API
axios.defaults.baseURL = 'http://localhost:5000/api';  // Flask backend
axios.defaults.withCredentials = true;  // Allow credentials (cookies) to be sent

// Intercept requests to add Authorization header with token
axios.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token');  // Access token stored in localStorage
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

new Vue({
  render: h => h(App)
}).$mount('#app');
