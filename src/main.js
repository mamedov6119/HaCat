import {createApp} from 'vue'
import {createRouter, createWebHistory} from 'vue-router'
import App from './App.vue'
import HelloWorld from './components/HelloWorld.vue'

const routes = [
    { path: '/', component: HelloWorld },
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