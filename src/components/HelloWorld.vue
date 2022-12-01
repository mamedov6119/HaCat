<template>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <h1 class="text-center">Welcome to the site <span style="color:blue; -webkit-text-stroke: .5px black ;">{{name}}</span></h1> 
        <button class="btn btn-primary" @click="startProcess">Start Process</button>
        <div class="display pc" >
          <div class="card m-auto mt-5" style="width: 70%;" v-if="(build.Money_left && build.Money_left * -1 <3400)">
            <div class="card-header">
              Your Build <span style="color:green">${{(build.Money_left * -1).toFixed(2)}}</span>
            </div>
            <div class="accordion accordion-flush" id="accordionExample">
           



              <div class="accordion-item" v-for="key in Object.keys(build)" v-bind:key="key">
                <div v-if="key != 'Money_left'">
                  <h2 class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" v-bind:data-bs-target="'#'+key" aria-expanded="true" v-bind:aria-controls="'#'+key">
                      <li class="list-group-item"><strong>{{(key[0].toUpperCase() + key.substring(1)).replace(/[_]/gm, " ")}}</strong>: {{build[key]['name']}} <span style="color:green">${{build[key]['price_usd']}}</span> </li>
                    </button>
                  </h2>
                <div v-bind:id="key" class="accordion-collapse collapse" aria-labelledby="??" data-bs-parent="#accordionExample"> 
                    <div class="accordion-body text-start">
                      <span v-for="element in Object.keys( build[key] )" v-bind:key="(key + ' ' + element)">
                        <span v-if="element == 'price_usd'">
                          <strong>{{(element[0].toUpperCase() + element.substring(1)).replace(/[_]/gm, " ")}}:</strong> <span style="color: green">${{build[key][element] ? build[key][element] : "(None)"}}</span><br>
                        </span>
                        <span v-else>
                          <strong>{{(element[0].toUpperCase() + element.substring(1)).replace(/[_]/gm, " ")}}:</strong> {{build[key][element] ? build[key][element] : "(None)"}} <br>
                        </span>
                      </span>
                    </div>
                  </div> 
                </div>
              </div>










            </div>
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
      this.build = await axios.get('http://localhost:9000/api/pc_parts/random_build/0').then(res =>
      {
       let data = res.data.data;
        data.Money_left = res.data.Money_left;
        return data
      } )
      this.recall();
      // ---------------------------------------------------THAT PART NEEDS TO BE CHANGED TO THE API CALL ,WHEN WILL BE PLACED ON THE SERVER -----------------------------------------
    },
     recall(){
     if (!this.build.Money_left || this.build.Money_left * -1 >3400){
      this.startProcess();
     }
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
