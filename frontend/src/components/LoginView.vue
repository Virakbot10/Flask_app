<template>
  <div>
    <h1>Login</h1>
    <button @click="login">Login with Keycloak</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginView',
  methods: {
    async login() {
      const backendUrl = 'http://localhost:5000/login';
      try {
        const response = await axios.get(backendUrl);
        if (response.data.access_token) {
          localStorage.setItem('access_token', response.data.access_token);
          localStorage.setItem('id_token', response.data.id_token);
          this.$router.push('/userinfo');
        }
      } catch (error) {
        console.error('Login failed:', error);
      }
    }
  }
}
</script>
