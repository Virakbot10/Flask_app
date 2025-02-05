import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/store.js' // Optional: If using Vuex for state management

const app = createApp(App)
app.use(router)
app.use(store) // Optional: If using Vuex
app.mount('#app')