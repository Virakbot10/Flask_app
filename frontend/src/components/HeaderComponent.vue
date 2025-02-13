<template>
  <header class="header">
    <div class="logo">DENSO</div>
    <nav class="nav">
      <a href="#">Home</a>
      <a href="#">Products</a>
      <a href="#">Services</a>
      <a href="#">About</a>
      <a href="#">Contact</a>
    </nav>
    <div v-if="user" class="user-info">
      <span>Welcome: {{ user.userinfo.name }}</span>
      <button @click="logout">Logout</button>
    </div>
  </header>
</template>

<script>
import apiClient from '@/utils/apiClient.js';

export default {
  data() {
    return {
      user: null
    };
  },
  async created() {
    await this.fetchUserInfo();
  },
  methods: {
    async fetchUserInfo() {
      try {
        const response = await apiClient.get('/api/userinfo');
        this.user = response.data;
      } catch (error) {
        console.error('Error fetching user info:', error);
        this.user = null;
      }
    },
    logout() {
      localStorage.removeItem('access_token'); // Clear token
      window.location.href = 'http://localhost:5000/logout'; // Redirect to Flask logout
    }
  }
}
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #fff;
  padding: 20px 40px;
  border-bottom: 1px solid #ddd;
}
.logo {
  font-size: 24px;
  font-weight: bold;
  color: #e60012; /* DENSO Red */
}
.nav a {
  margin: 0 15px;
  text-decoration: none;
  color: #333;
}
.nav a:hover {
  color: #e60012;
}
.user-info {
  display: flex;
  align-items: center;
}
.user-info span {
  margin-right: 15px;
}
button {
  padding: 8px 16px;
  background-color: #e60012;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #b3000e;
}
</style>
