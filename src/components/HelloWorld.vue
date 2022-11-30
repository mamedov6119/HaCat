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
              <div class="accordion-item">
                <h2 class="accordion-header" id="headingOne">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                    <li class="list-group-item">motherboard : {{ "motherboard" in build ? build.motherboard.name : '' }}  <span style="color:green">${{build.motherboard.price_usd}}</span> </li>
                  </button>
                </h2>
                <div id="collapseOne" class="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                  <div class="accordion-body text-start " >
                    <strong>Name : </strong> {{ "motherboard" in build ? build.motherboard.name : '' }} <br>
                    <strong>Rating :</strong> {{ "motherboard" in build ? build.motherboard.rating : '' }} <br>
                    <strong>rating count:</strong> {{ "motherboard" in build ? build.motherboard.rating_count : '' }} <br>
                    <strong>price:</strong> <span style="color:green">${{ "motherboard" in build ? build.motherboard.price_usd : '' }}</span> <br>
                    <strong>socket/cpu:</strong> {{ "motherboard" in build ? build.motherboard["socket_/_cpu"] : '' }} <br>
                    <strong>form factor:</strong> {{ "motherboard" in build ? build.motherboard.form_factor : '' }} <br>
                    <strong>memory max:</strong> {{ "motherboard" in build ? build.motherboard.memory_max : '' }} <br>
                    <strong>memory slots:</strong> {{ "motherboard" in build ? build.motherboard.memory_slots : '' }} <br>
                    <strong>color:</strong> {{ "motherboard" in build ? build.motherboard.color : '' }} <br>
                  </div>
                </div>
              </div>
              <div class="accordion-item">
                <h2 class="accordion-header" id="headingOne">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="true" aria-controls="collapseTwo">
                    <li class="list-group-item">memory RAM : {{ "motherboard" in build ? build.memory.name : '' }}  <span style="color:green">${{build.memory.price_usd}}</span> </li>
                  </button>
                </h2>
                <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                  <div class="accordion-body text-start " >
                    <strong>Name : </strong> {{ "memory" in build ? build.memory.name : '' }} <br>
                    <strong>Rating :</strong> {{ "memory" in build ? build.memory.rating : '' }} <br>
                    <strong>rating count:</strong> {{ "memory" in build ? build.memory.rating_count : '' }} <br> 
                    <strong>price: </strong> <span style="color:green">${{ "memory" in build ? build.memory.price_usd : '' }} </span>  <br> 
                    <strong>speed:</strong> {{ "memory" in build ? build.memory.speed : '' }} <br>
                    <strong>modules:</strong> {{ "memory" in build ? build.memory.modules : '' }} <br>
                    <strong>price/gb:</strong> <span style="color:green">{{ "memory" in build ? build.memory["price_/_gb"] : '' }} </span> <br>
                    <strong>color:</strong> {{ "memory" in build ? build.memory.color : '' }} <br>
                    <strong>first_word_latency:</strong> {{ "memory" in build ? build.memory.first_word_latency : '' }} <br>
                    <strong>cas_latency:</strong> {{ "memory" in build ? build.memory.cas_latency : '' }} <br>
                  </div>
                </div>
              </div>
            </div>
            <ul  class="list-group list-group-flush">
              <li class="list-group-item">Case Accessory: {{ "case_accessory" in build ? build.case_accessory.name : ''  }} <span style="color:green">${{build.case_accessory.price_usd}}</span> </li>
              <li class="list-group-item">case fan: {{ "case_fan" in build ? build.case_fan.name : '' }} <span style="color:green">${{build.case_fan.price_usd}}</span> </li>
              <li class="list-group-item">case: {{ "case" in build ? build.case.name : '' }}  <span style="color:green">${{build.case.price_usd}}</span> </li>
              <li class="list-group-item">cpu cooler: {{ "cpu_cooler" in build ? build.cpu_cooler.name : '' }}  <span style="color:green">${{build.cpu_cooler.price_usd}}</span> </li>
              <li class="list-group-item">cpu: {{ "cpu" in build ? build.cpu.name : '' }}  <span style="color:green">${{build.cpu.price_usd}}</span> </li>
              <li class="list-group-item">user video card: {{ "video_card" in build ? build.video_card.name : '' }}  <span style="color:green">${{build.video_card.price_usd}}</span> </li>
              <li class="list-group-item">external hard drive: {{ "external_hard_drive" in build ? build.external_hard_drive.name : '' }}  <span style="color:green">${{build.external_hard_drive.price_usd}}</span> </li>
              <li class="list-group-item">headphones: {{ "headphones" in build ? build.headphones.name : '' }}  <span style="color:green">${{build.headphones.price_usd}}</span> </li>
              <li class="list-group-item">internal hard drive: {{ "internal_hard_drive" in build ? build.internal_hard_drive.name : '' }}  <span style="color:green">${{build.case_fan.price_usd}}</span> </li>
              <li class="list-group-item">keyboard : {{ "keyboard" in build ? build.keyboard.name : '' }}  <span style="color:green">${{build.keyboard.price_usd}}</span> </li> 
              <li class="list-group-item">monitor : {{ "monitor" in build ? build.monitor.name : '' }}  <span style="color:green">${{build.monitor.price_usd}}</span> </li>
              <li class="list-group-item">mouse : {{ "mouse" in build ? build.mouse.name : '' }}  <span style="color:green">${{build.mouse.price_usd}}</span> </li>
              <li class="list-group-item">power supply : {{ "power_supply" in build ? build.power_supply.name : '' }}  <span style="color:green">${{build.power_supply.price_usd}}</span> </li>
              <li class="list-group-item">speakers: {{ "speakers" in build ? build.speakers.name : '' }}  <span style="color:green">${{build.speakers.price_usd}}</span> </li>
              <li class="list-group-item">thermal paste: {{ "thermal_paste" in build ? build.thermal_paste.name : '' }}  <span style="color:green">${{build.thermal_paste.price_usd}}</span> </li>
              <li class="list-group-item">webcam: {{ "webcam" in build ? build.webcam.name : '' }}  <span style="color:green">${{build.webcam.price_usd}}</span> </li>
              <li class="list-group-item">wireless network card: {{ "wireless_network_card" in build ? build.wireless_network_card.name : '' }}  <span style="color:green">${{build.wireless_network_card.price_usd}}</span> </li>

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
