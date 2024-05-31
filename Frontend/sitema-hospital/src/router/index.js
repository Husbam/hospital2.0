import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import LoginView from '../components/login.vue'
import registerUser from '../components/registerUser.vue'
import dashboardView from '../components/dashboard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: registerUser
    },
    {
      path: '/dashboard',
      name: 'dasboard',
      component: dashboardView
    }
  ]
})

export default router
