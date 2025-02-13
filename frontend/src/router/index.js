// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/components/LandingPage.vue';
// import AboutPage from '@/components/AboutPage.vue'; // example additional page

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: LandingPage
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   component: AboutPage
  // }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return {...savedPosition, behavior: 'smooth'};
    } else {
      return {top: 0, behavior: 'smooth'};
    }
  }
});

export default router;
