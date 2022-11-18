<template>
  <nav class="navbar navbar-dark bg-dark fixed-top">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand">Home</router-link>
      <router-link to="/">
        <img src="./assets/white.png" alt="">
      </router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="offcanvas offcanvas-start text-bg-dark" tabindex="-1" id="offcanvasDarkNavbar" aria-labelledby="offcanvasDarkNavbarLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasDarkNavbarLabel">Dark offcanvas</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/users"  v-if="isAdmin">Users</router-link>
            </li>
            <li class="nav-item" v-if="isUser">
              <a class="nav-link" @click="logout">Logout</a>
              </li>
            <li class="nav-item" v-else>
              <router-link class="nav-link" to="/login">Login</router-link>
            </li>
            <li class="nav-item dropdown" v-if="isAdmin">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false" >
                Administation Tools
              </a>
              <ul class="dropdown-menu dropdown-menu-dark">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li>
                  <hr class="dropdown-divider">
                </li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li>
          </ul>
          
        </div>
      </div>
    </div>
  </nav>
  <router-view id="router"></router-view>
</template>

<script>

export default {
  name: 'App',
  components: {},
  data() {
    return {
      isAdmin: false,
      isUser: window.localStorage.getItem('user') != null
    }
  },
  created(){
    if(this.isUser){
      this.isAdmin = JSON.parse(window.localStorage.getItem('user')).admin == 1
    }
  },
  methods: {
    logout() {
      window.localStorage.removeItem('user')
      this.isUser = false
      alert('You have been logged out')
      this.$router.go()
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding: 200px 0;
}
img {
  width: auto;
  height: 120px;
}
.navbar-brand {
  color: chartreuse;
}
.navbar-brand:hover {
  color: rgb(255, 255, 255);
}

</style>
