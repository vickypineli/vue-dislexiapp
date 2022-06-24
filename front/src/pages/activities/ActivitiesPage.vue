<template>
  <div class="activites-container">
    <h1>JARDUERAK </h1>
    <section class="box-activities">
          <router-link to="/activities/word-by-word"><button>HITZEZ HITZ</button></router-link>
          <router-link to="/activities/play-word-by-word"><button>IRAKUR-LAGUN</button></router-link>
          <router-link to="/activities/count-letters"><button>SILABAK ZENBATU</button></router-link>
          <router-link to="/activities/chained-words"><button>HITZ KATEATUAK</button></router-link>
          <!-- <router-link to="/activities/color-memory"><button>MARGOTU ZURE MEMORIA</button></router-link>
          <router-link to="/activities/cards-game"><button>BIKOTE JOLASA</button></router-link> -->
    </section>
    <!-- <section>
      <button v-for="activity in activities" :key="activity.id" @click="onButtonClicked(activity)">{{activity.name}}</button>
    </section>

  <p>{{localUser}}</p> -->
    </div>
</template>

<script>
import { useStorage } from "@vueuse/core";
import config from "@/config.js";

export default {
  name:"ActivityPage",
 
  data() {
    return {
      activity: "",
      activities: [],
      localUser: useStorage("user", {}),
    }
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const settings = {
        method: "GET",
        headers: {
          Authorization: localStorage.user_id,
        },
      };
      const response = await fetch(`${config.API_PATH}/activities`, settings);
      this.activities = await response.json();
    },
    onButtonClicked(activity){
      this.$router.push(`/activities/${activity.route.toLowerCase()}`);        
    }
  }
  };
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Slackey&display=swap');
.activites-container{
    width: 90vw;
    padding-top: 50px;
    margin: auto;
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
}
.box-activities{
  width: 90%;
  height: 90%;
  display: flex;
  justify-content: center;
  flex-wrap:wrap;
  margin: auto;

}
h1{
  width: 90vw;
  height: 40px;
  padding: 30px;
  margin: auto;
  font-size:2.4em ;
  font-family: 'Slackey';
  text-transform: uppercase;
  color: rgb(242, 117, 8);
}
button{
  width: 300px;
  height: 100px;
  margin: 10px;
  border-radius: 10px;
  font-size: 1em;
  border-color:gray;
  border-radius: 15px;
  font-size: 1.5em;
  font-weight: bold;
 
  background: #42b983;
  color:white;
  
}
</style>
