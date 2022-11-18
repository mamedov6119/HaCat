<template>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <h1 class="text-center">Welcome to the site <span style="color:blue; -webkit-text-stroke: .5px black ;">{{name}}</span></h1>
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
export default {
  name: 'HelloWorld',
  props: {},
  data() {
    return {
      name: ''
    }
  },
  created() {
    if(window.localStorage.getItem('user') != null){
      this.name = JSON.parse(window.localStorage.getItem('user')).name
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
