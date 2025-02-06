<template>
  <router-view/>
</template>

<script>
export default {
  name: 'App',
  mounted() {
    this.checkAuthStatus();
  },
  methods: {
    async checkAuthStatus() {
      try {
        const response = await fetch('http://localhost:5000/api/user', {
          credentials: 'include'
        });
        
        if (response.ok) {
          const data = await response.json();
          if (data.authenticated) {
            // User is authenticated, redirect to home
            this.$router.push('/');
          } else {
            // User is not authenticated, redirect to login
            this.$router.push('/login');
          }
        }
      } catch (error) {
        console.error('Authentication check failed:', error);
      }
    }
  }
}
</script>