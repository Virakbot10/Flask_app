<template>
  <router-view/>
</template>

<script>
export default {
  name: 'App',
  mounted() {
    this.checkAuth()
  },
  methods: {
    async checkAuth() {
      try {
        const response = await fetch('http://localhost:5000/api/user', {
          credentials: 'include'
        })
        
        if (response.ok) {
          this.$store.commit('setUser', await response.json())
        }
      } catch (error) {
        console.error('Auth check failed:', error)
      }
    }
  }
}
</script>