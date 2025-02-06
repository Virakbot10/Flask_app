<template>
  <div>
    <h1>Login</h1>
    <a :href="loginUrl">Login with Keycloak</a>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loginUrl: 'http://localhost:5000/api/login'
    }
  }
}
</script>