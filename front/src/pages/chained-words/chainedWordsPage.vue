<template>
    <h1>HITZ KATEATUAK</h1>
    <section class="exerxice-container" v-for="phrase in phrases" :key="phrase.id">
          <div class="e">          
              <p>{{phrase.level}}</p>
          </div>

    </section>
</template>
<script>
export default {
  name:"ChainedWord",
  data() {
        return {
            phrase:"",
            phrases:[], 
        }

  },
  mounted() {
        this.loadData();
  },

  methods: {
        async loadData() {
        const response = await fetch(
            "http://localhost:5000/api/activities/chainedword"
        );
        this.phrases = await response.json();
        },
  }
} 
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Slackey&display=swap");

h1 {
  width: 90vw;
  height: 40px;
  margin: auto;
  font-size:2.0em ;
  font-family: 'Slackey';
  text-transform: uppercase;
  color: rgb(242, 117, 8);
}
</style>