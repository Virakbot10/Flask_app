<!-- src/App.vue -->
<template>
  <div>
    <!-- Check if keycloak and tokenParsed exist -->
    <div v-if="keycloak && keycloak.tokenParsed">
      <h1>Welcome, {{ keycloak.tokenParsed.preferred_username }}</h1>
      <p>Your email: {{ keycloak.tokenParsed.email }}</p>
      <button @click="fetchProtectedData">Fetch Protected Data</button>
      <div v-if="protectedData">
        <h2>Protected Data from Flask</h2>
        <pre>{{ protectedData }}</pre>
      </div>
    </div>
    <!-- Fallback if keycloak data isn't available yet -->
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { inject, ref } from "vue";

export default {
  name: "App",
  setup() {
    const keycloak = inject("keycloak");
    const protectedData = ref(null);

    const fetchProtectedData = async () => {
      try {
        const response = await axios.get("/api/protected", {
          headers: { Authorization: `Bearer ${keycloak.token}` },
        });
        protectedData.value = response.data;
      } catch (error) {
        console.error("Error fetching protected data:", error);
      }
    };

    return { keycloak, fetchProtectedData, protectedData };
  },
};
</script>
