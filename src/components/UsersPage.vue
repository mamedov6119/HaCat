<template>
  <div>
    <form class="w-50 m-auto text-start">
      <div class="mb-2">
        <label for="">Nickame</label>
        <input class="form-control" type="text" name="" id="name">
      </div>
      <div class="mb-2">
        <label for="">Email</label>
        <input class="form-control" type="email" name="" id="email">
      </div>
      <div class="mb-4">
        <label for="">Password</label>
        <input class="form-control" type="password" name="" id="password">
      </div>
      <button @click="newUser" class="btn btn-success w-100 text-center mb-5">register</button>
    </form>
  </div>
  <ul class="list-group px-4">
    <li class="list-group-item list-group-item-action text-start" v-for="(user,index) in users" v-bind:key="index" v-on:click="removeUser($event, user._id.$oid)">
        <div class="row">
          <div class="col-8">
            <p>Name: <b class="text-start">{{user.name}}</b></p>
          </div>
          <div class="col-4">
            <p class="text-end text-muted">id: {{user._id.$oid}}</p>
          </div>
        </div>
        <p>{{user.email}}</p>
    </li>
  </ul>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UsersPage',
  data() {
    return {users: []}
  },
  async created() {
    this.updateUsers()
  },
  methods: {
    async updateUsers() {
      this.users = await axios.get('http://localhost:5000/api/all_users/').then(a => a.data)
    },
    async newUser(e) {
      e.preventDefault()
      await axios.post('http://localhost:5000/api/create_user', {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
        admin: 0
      })
      this.updateUsers()
    },
    async removeUser(e, id) {
      e.preventDefault();
      await axios.delete('http://localhost:5000/api/del_by_id/'+id);
      this.updateUsers()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
p {
  margin-bottom: 0;
}
</style>