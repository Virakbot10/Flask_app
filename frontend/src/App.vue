<template>
  <div id="app">
    <!-- Optionally, you can include a global header or navigation -->
    <HeaderComponent />
    <!-- This is where the routed components will be rendered -->
    <router-view />
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue';
import FooterComponent from '@/components/FooterComponent.vue';

export default {
  components: {
    HeaderComponent,
    FooterComponent
  }
}
</script>

<style scoped>
/* your global app styles */
</style>
