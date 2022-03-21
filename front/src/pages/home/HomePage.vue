<template>
  <div class="home">
      <div>
        <h1>IRLA-KURRI</h1>
        </div>
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

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Slackey&display=swap');
h1 {
  font-style: italic;
  font-family: 'Slackey';
}
h1 {
  

 
 
  transform-origin: bottom center;
  -webkit-transform-origin: bottom center;
  text-transform: uppercase;
}
</style>
