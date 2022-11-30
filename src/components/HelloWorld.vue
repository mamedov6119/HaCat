<template>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <h1 class="text-center">Welcome to the site <span style="color:blue; -webkit-text-stroke: .5px black ;">{{name}}</span></h1> 
        <button class="btn btn-primary" @click="startProcess">Start Process</button>
        <div class="display pc" >
          <div class="card m-auto mt-5" style="width: 70%;">
            <div class="card-header">
              Your Build
            </div>
            <ul  class="list-group list-group-flush">
              <li class="list-group-item">Case Accessory: {{ "case" in build ? build.case.name : '' }} </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <users-page></users-page>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';



export default {
  name: 'HelloWorld',
  props: {},
  data() {
    return {
      name: '',
      build : {}
    }
  },
  created() {
    if(window.localStorage.getItem('user') != null){
      this.name = JSON.parse(window.localStorage.getItem('user')).name
    }
  },
  methods: {
    async startProcess(){

      this.build = await axios.get('http://localhost:9000/api/pc_parts/random_build/5000').then(res => res.data.data)  
      console.log(this.build.case)

      // ---------------------------------------------------THAT PART NEEDS TO BE CHANGED TO THE API CALL ,WHEN WILL BE PLACED ON THE SERVER -----------------------------------------
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
