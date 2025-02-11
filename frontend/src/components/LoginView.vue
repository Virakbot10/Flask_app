<template>
  <div class="login">
    <h1>Login</h1>
    <button @click="login">Login with Keycloak</button>
  </div>
</template>

<script>
export default {
  methods: {
    login() {
      window.location.href = 'http://localhost:5000/login';
    }
  }
}
</script>

<style scoped>
.login {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>
