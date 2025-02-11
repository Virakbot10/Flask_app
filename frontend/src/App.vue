<template>
  <div id="app">
    <header>
      <h1>Welcome to the App</h1>
      <p v-if="user">Logged in as: {{ user.userinfo.name }}</p>
      <button v-if="user" @click="logout">Logout</button>
    </header>
  </div>
</template>

<script>
import axios from 'axios';

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
        const response = await axios.get('/api/userinfo');
        this.user = response.data;
      } catch (error) {
        console.error('Error fetching user info:', error);
        this.login();
      }
    },
    login() {
      window.location.href = 'http://localhost:5000/login';
    },
    logout() {
      window.location.href = 'http://localhost:5000/logout';
    }
  }
}
</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
}

header {
  margin-bottom: 2rem;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>
