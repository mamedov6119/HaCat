<template>
  <ul class="nav nav-tabs tab" id="myTab" role="tablist">
    <li class="nav-item w-50" role="presentation">
      <button class="nav-link w-100 active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Login</button>
    </li>
    <li class="nav-item w-50" role="presentation">
      <button class="nav-link w-100" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Registration</button>
    </li>
  </ul>

  <div class="tab-content border contents" id="myTabContent">
    <div class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
      <form class="p-2">
        <div class="mb-3">
          <label for="login_email" class="form-label">Email address</label>
          <input type="email" class="form-control" id="login_email" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
          <label for="login_password" class="form-label">Password</label>
          <input type="password" class="form-control" id="login_password">
        </div>
        <button type="submit" class="btn btn-primary" @click="login">Submit</button>
      </form> 
    </div>
    <div class="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">
      <form class="p-2">
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Name</label>
          <input type="text" class="form-control" id="name" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Email address</label>
          <input type="email" class="form-control" id="email" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Password</label>
          <input type="password" class="form-control" id="password">
        </div>
        <button type="submit" class="btn btn-primary" @click="newUser">Submit</button>
      </form> 
    </div>
  </div>
  
</template>

<script>
import axios from 'axios';
export default {
  name: 'LoginPage',
  created() {
    if (localStorage.getItem('user')) {
      this.$router.push({name: 'home'})
    }
  },
  methods: {
    async newUser(e) {
      e.preventDefault()
      await axios.post('http://localhost:9000/api/create_user', {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
        admin: 0
      })
    },
    async login(e) {
      e.preventDefault()
      let email = document.getElementById('login_email').value;
      let password = document.getElementById('login_password').value;
      let result = await axios.get('http://localhost:9000/api/login/' + email + '/' + password, {})
      if (result.data.length > 0) {
        let user = { id: result.data[0].id, name: result.data[0].name, email: result.data[0].email, admin: result.data[0].admin }
        localStorage.setItem('user', JSON.stringify(user))
        console.log(localStorage.getItem('user'))
        alert('Login successful')
        this.$router.go()
      } else {
        alert('Invalid login')
      } 
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.tab, .contents {
  width: 50%;
  margin: auto;
  text-align: start;
}
.contents {
  border-top: none !important;
}
</style>
