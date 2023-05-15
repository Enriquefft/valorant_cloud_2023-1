import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import AgentsView from '../views/AgentsView.vue'
import Test from '../views/TestView.vue'
import PlayerInfo from  '../views/PlayerInfoView.vue'
import LoginView from  '../views/LoginView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/users',
      name: 'users',
      component: LoginView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AboutView
    },
    {
      path: '/agents',
      name: 'agents',
      component: AgentsView
    },
    {
      path: '/test',
      name: 'test',
      component: Test
    },
    {
      path: '/playerinfo',
      name: 'playerinfo',
      component: PlayerInfo
    }
  ]
})

export default router
