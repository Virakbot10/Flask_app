<template>
    <div>
      <h1>User Info</h1>
      <pre>{{ userInfo }}</pre>
      <button @click="logout">Logout</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'UserInfo',
    data() {
      return {
        userInfo: null
      };
    },
    async mounted() {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        try {
          const response = await axios.get('http://localhost:5000/user', {
            headers: { Authorization: `Bearer ${accessToken}` }
          });
          this.userInfo = response.data.user;
        } catch (error) {
          console.error('Failed to fetch user info:', error);
        }
      } else {
        this.$router.push('/login');
      }
    },
    methods: {
      logout() {
        this.$router.push('/logout');
      }
    }
  }
  </script>
  