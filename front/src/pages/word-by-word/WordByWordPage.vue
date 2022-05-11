<template>
  <div>
    <h1>HITZEZ-HITZ</h1>
  </div>
  <section class="container">
    <div class="text">
      <h1 :style="fontSelected">{{ word }}</h1>
    </div>
  
    <div class="button-container">
      <button @click="PlayText()">PLAY</button>
      <button @click="PauseText()">STOP</button>
    </div>
  </section>
  <section class="settings">
    
    <div class="aukera">
      <label> Aukeratu testua: </label>
      <select v-model="textSelected">
        <option v-for="text in texts" :key="text" :value="text.text">
          {{ text.language }}
        </option>
      </select>
      <label> letra-tipo: </label>
      <select v-model="fontSelected">
        <option :value="escolar" :style="escolar">ESCOLAR</option>
        <option :value="dislexia" :style="dislexia">DISLEXIA</option>
        <option :value="sarakanda" :style="sarakanda">SARAKANDA</option>
      </select>
      <label> Hitz-min: </label>
      <input class="slider"  v-model="wordsByMinute" type="range" min="10" max="90"/>
    </div>
    <textarea
      v-model="textSelected"
      placeholder="Aukeratu testua....."
      :style="fontSelected"
    ></textarea>
  </section>
</template>

<script>
export default {
  name: "Word-by-word",
  data() {
    return {
      word: "",
      wordsByMinute: 0,
      textByWords: [],
      play: 0,
      texts: [],
      textSelected: "",
      escolar: {
        fontFamily: "escolar",
        color: "blue",
      },
      dislexia: {
        fontFamily: "dislexia",
        color: "green",
      },
      sarakanda: {
        fontFamily: "sarakanda",
        color: "red",
      },
    };
  },
  computed: {
    timeInterval() {
      return this.wordsByMinute * 100;
    },
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch(
        "http://localhost:5000/api/activities/wordbyword"
      );
      this.texts = await response.json();
    },

    PauseText() {
      this.pause = clearInterval(this.play);
    },

    PlayText() {
      this.textByWords = this.textSelected.split(" ");

      let item = 0;
      this.play = setInterval(() => {
        this.word = this.textByWords[item];
        item += 1;
      }, this.timeInterval);
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Slackey&display=swap");

body{
  background-image: url("https://i.ibb.co/PgXQTyG/5086.jpg");
}
.container {
  margin: 5px;
  display: flex;
  height: 200px;
  
}
.text{
  border: 1px solid gray;
  border-radius: 10px;
  flex: auto;
  font-size: 2.5em;
  background: white;
}
.button-container{
  width: 130px;
}
button{
  display: block;
  font-size: 20px;
  padding: 8px;
  margin: 30px;
  border-radius: 15px;
}
.settings {
  margin: 5px;
  display: flex;
  flex-direction: column;
  height: 200px;
}
.aukera{
  display: flex;
  flex-direction: row;
  width: 230px;
}
textarea {
  font-size: 1.2em;
  border-radius: 10px;
  width: 90vw;
  height: 20vh;
}
select {
  font-size: large;
  margin: 25px;
}
.slidecontainer {
  width: 100%;
}


.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 25px;
  height: 25px;
  background: #04AA6D;
  cursor: pointer;
}



</style>