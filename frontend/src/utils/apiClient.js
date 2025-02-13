import axios from 'axios';

// Create an axios instance with global settings
const apiClient = axios.create({
  baseURL: 'http://localhost:5000/', // Flask backend URL
  withCredentials: true // Ensures cookies/session are sent
});

// Add an interceptor to check for 401 responses
apiClient.interceptors.response.use(
  response => response, // Pass through if successful
  error => {
    if (error.response && error.response.status === 401) {
      console.warn('Session expired or invalid. Redirecting to login.');
      window.location.href = 'http://localhost:5000/login';
    }
    return Promise.reject(error);
  }
);

export default apiClient;
