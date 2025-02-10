<template>
  <div>
    <h1>Logout</h1>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LogoutView',
  methods: {
    async logout() {
      localStorage.removeItem('access_token');
      localStorage.removeItem('id_token');

      const backendUrl = 'http://localhost:5000/logout';
      try {
        await axios.get(backendUrl);
        this.$router.push('/');
      } catch (error) {
        console.error('Logout failed:', error);
      }
    }
  }
}
</script>
