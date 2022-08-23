<template>
  <div id="app">
    <b-form-group id="input-group-2" label="Input todo:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="input"
          placeholder="Enter name"
          @keyup.enter="sendTodo"
          required
        ></b-form-input>
      </b-form-group>
    <div class="todos">
      <div class="list" v-for="item in data" :key="item.id">
        <input type="checkbox" :checked="item.status === 'done'" />
        <h3 :class="{'line-through': item.status === 'done'}">{{ item.description }}</h3>
        <span @click="removeItem(item.id)" style="cursor: pointer">X</span>
      </div>

    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'App',
  data(){
    return {
      input: '',
      data: [],
      done: false,
      checked: false
    }
  },
  methods: {
    removeItem(id){
      axios.post('http://127.0.0.1:8000/api/remove-task/', {'id': id}).then((res) => {
        if(res.data.success){
          this.input = ''
          this.getData()
        }
      })
    },
    sendTodo(){
      axios.post('http://127.0.0.1:8000/api/create-task/', {'description': this.input}).then((res) => {
        if(res.data.success){
          this.input = ''
          this.getData()
        }
      })
    },
    getData(){
      axios.get('http://127.0.0.1:8000/api/get-tasks/').then((res) => {
      this.data = res.data
    })
    },
  },
  mounted() {
    this.getData()
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
  width: 60%;
  margin: 50px auto;
}
.todos .list{
  display: flex;
  justify-content: space-around;
  align-items: center;
  vertical-align: center;
  margin-top: 20px;
}
.line-through {
  text-decoration: line-through !important;
}
p{
  margin: 0 !important;
  padding: 0 !important;
}
</style>
