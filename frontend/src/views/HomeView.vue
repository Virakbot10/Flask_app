<template>
  <div v-if="user.authenticated">
    <h1>Welcome {{ user.username }}!</h1>
    <button @click="logout">Logout</button>
  </div>
  <div v-else>
    <a href="/login">Login</a>
  </div>
</template>

<script>
export default {
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  methods: {
    async logout() {
      await fetch('http://localhost:5000/api/logout', {
        credentials: 'include'
      })
      this.$store.commit('clearUser')
      this.$router.push('/login')
    }
  }
}
</script>