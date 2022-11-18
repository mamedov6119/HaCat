import {createApp} from 'vue'
import {createRouter, createWebHistory} from 'vue-router'
import App from './App.vue'
import HelloWorld from './components/HelloWorld.vue'
import LoginPage from './components/LoginPage.vue'
import UsersPage from './components/UsersPage.vue'
import AddComponents from './components/AddComponents.vue'


const routes = [
  { path: '/', component: HelloWorld, name: 'home' },
  { path: '/login', component: LoginPage, name: 'login' },
  { path: '/users', component: UsersPage,  name: 'users' },
  { path: '/components', component: AddComponents, name: 'components' },
]
  
  const router = createRouter({
    history: createWebHistory(),
    routes, // short for `routes: routes`
  })
  
  const app = createApp(App)
  app.use(router)

  router.isReady().then(() => {
    app.mount('#app');
  })