<template>
  <div class="home">
      <div>
        <h1>IRLA-KURRI</h1>
    
      </div>
       <router-link to="/activities"
    ><button>SARTU</button></router-link>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      info: {}
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/activities')
      this.info = await response.json()
    }
  }


}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Slackey&display=swap');
h1 {
  font-style: italic;
  font-family: 'Slackey';
  text-transform: uppercase;
}
button {
  margin: 10px;
  padding: 5px 10px;
  border-color:gray;
  border-radius: 25px;
  font-size: 1em;
  background: #42b983;
  color:white;
}
</style>
