// src/keycloak.js
import Keycloak from 'keycloak-js';

const keycloak = new Keycloak({
  url: 'http://localhost:8080', // URL to your Keycloak server (adjust if needed)
  realm: 'myrealm',                  // Your Keycloak realm name
  clientId: 'vue_frontend'              // Your Keycloak client ID
});

export default keycloak;