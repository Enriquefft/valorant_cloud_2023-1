import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import AgentsView from '../views/AgentsView.vue'
import Test from '../views/TestView.vue'
import PlayerInfo from  '../views/PlayerInfoView.vue'
import UsersView from  '../views/UsersView.vue'
import PlayersView from  '../views/PlayersView.vue'
import MatchesView from  '../views/MatchesView.vue'

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
      component: UsersView
    },
    {
      path: '/players',
      name: 'players',
      component: PlayersView
    },
    {
      path: '/matches',
      name: 'matches',
      component: MatchesView
    },
    {
      path: '/agents',
      name: 'agents',
      component: AgentsView
    },
  ]
})

export default router
