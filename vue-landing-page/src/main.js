// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import keycloak from './keycloak';

keycloak.init({ onLoad: 'login-required' })
  .then(authenticated => {
    if (authenticated) {
      console.log("Keycloak initialized, tokenParsed:", keycloak.tokenParsed);
      createApp(App)
        .provide('keycloak', keycloak)
        .mount('#app');
    } else {
      window.location.reload();
    }
  })
  .catch(error => {
    console.error('Keycloak initialization error:', error);
  });
