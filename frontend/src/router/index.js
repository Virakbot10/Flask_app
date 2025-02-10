import Vue from 'vue';
import Router from 'vue-router';
import Login from '@/components/LoginView.vue';
import Logout from '@/components/LogoutView.vue';
import UserInfo from '@/components/UserInfo.vue';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/logout',
      name: 'Logout',
      component: Logout
    },
    {
      path: '/userinfo',
      name: 'UserInfo',
      component: UserInfo,
      meta: { requiresAuth: true }
    }
  ]
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const token = localStorage.getItem('access_token');

  if (requiresAuth && !token) {
    next({ path: '/', query: { redirect: to.fullPath } });
  } else {
    next();
  }
});

export default router;
