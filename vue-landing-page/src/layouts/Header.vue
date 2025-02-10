<script setup>
import { ref } from 'vue';

const props = defineProps({
  userInfo: {
    type: Object,
    default: () => ({})
  }
});

const emit = defineEmits(['logout']);

const mobileNav = ref(false);

const toggleMobileNav = () => {
  mobileNav.value = !mobileNav.value;
};

const handleLogout = () => {
  emit('logout');
};
</script>

<template>
  <div class="container mx-auto px-5">
    <header class="flex justify-between py-4 items-center">
      <div>
        <p class="font-semibold" style="font-size: xx-large;">
          Welcome, {{ userInfo.name || userInfo.preferred_username || 'User' }}
        </p>
        <p class="text-lg text-gray-700">{{ userInfo.email }}</p>
      </div>

      <nav class="flex justify-end flex-col md:flex-row">
        <button @click="toggleMobileNav" type="button" class="flex md:hidden focus:outline-none">
          <svg viewBox="0 0 24 24" class="h-6 w-6 fill-current">
            <path fill-rule="evenodd" d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"></path>
          </svg>
        </button>

        <ul class="space-x-10 font-medium items-center hidden md:flex">
            <li class="uppercase hover:text-theme-secondary transition duration-200"><a href="#features" v-smooth-scroll>Features</a></li>
            <li class="uppercase hover:text-theme-secondary transition duration-200"><a href="#faq" v-smooth-scroll>FAQ</a></li>
            <li class="uppercase hover:text-theme-secondary transition duration-200"><a href="#subscribe" v-smooth-scroll>Subscribe</a></li>
          <li>
            <button @click="handleLogout" class="px-4 py-2 bg-red-500 text-white rounded">
              Logout
            </button>
          </li>
        </ul>
      </nav>
    </header>
  </div>
</template>

<style scoped>
.container {
  padding: 20px;
}
nav button {
  background-color: #007bff;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s;
}
nav button:hover {
  background-color: #0056b3;
}
</style>
