<template>
  <div>
    <h1>HITZEZ-HITZ</h1>
  </div>
  <section class="text-container">
    <div class="text">
      <h1 :style="fontSelected">{{ word }}</h1>
    </div>
    <div class="button-container">
      <button @click="PlayText()">PLAY</button>
      <button @click="PauseText()">STOP</button>
    </div>
  </section>
  <section class="options">
    <div class="option-item">
      <label> Aukeratu Testua: </label>
      <select v-model="textSelected">
        <option v-for="text in texts" :key="text" :value="text.text">
          {{ text.language }}
        </option>
      </select>
    </div>
    <div class="option-item">
      <label> Letra-tipo: </label>
      <select v-model="fontSelected">
        <option :value="escolar" :style="escolar">ESCOLAR</option>
        <option :value="dislexia" :style="dislexia">DISLEXIA</option>
        <option :value="sarakanda" :style="sarakanda">SARAKANDA</option>
      </select>
      </div>
    <div class="option-item">
      <div class="range">
      <label> Hitz-min:</label>{{ wordsByMinute }}
      </div>
      <input class="slider" list="tickmarks" v-model="wordsByMinute" type="range" max="120" min="30"  step="10"/>
      <datalist id="tickmarks">
      <option value="30"></option>
      <option value="60"></option>
      <option value="90"></option>
      <option value="120"></option>
      </datalist>
    </div>
  </section>  
    <textarea
      v-model="textSelected"
      placeholder="Aldatu testua hemen....."
      :style="fontSelected"
    ></textarea>
  
</template>

<script>
export default {
  name: "Word-by-word",
  data() {
    return {
      word: "",
      wordsByMinute: 10,
      textByWords: [],
      play: 0,
      texts: [],
      textSelected: "",
      output: 0,
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

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Slackey&display=swap");

body{
  background-image: url("https://i.ibb.co/MhBFzhC/paisaje.png");
}
.text-container {
  margin: 5px;
  display: flex;
  height: 200px;
  background: white;
  border: 1.5px solid rgb(3, 97, 3);
  border-radius: 10px;
}
.text{
  flex: auto;
  font-size: 3em;
}
.button-container{
  width: 20vw;
}
button{
  display: block;
  font-size: 20px;
  padding: 8px;
  margin: 30px;
  border-radius: 15px;
  border-color: rgb(41, 194, 41);
  background: rgb(34, 185, 34);
  color:white;
}
.options {
  margin-top: 10px;
  margin-bottom: 20px;
  display: flex;
  flex-direction: row;
}
.option-item{
  display: flex;
  flex-direction: column;
  width: 35vw;
  margin: 15px;
}
.range{
  margin: 5px;

}
textarea {
  font-size: 1.3em;
  border-radius: 10px;
  border-color: darkgreen;
  width: 95vw;
  height: 20vh;
  background: rgba(255, 255, 255, 0.73);
}
label{
  margin: 5px;
  font-size: 1.2em;
}
select {
  font-size: 1.2em;
}
.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 25px;
  height: 25px;
  background: whitesmoke;
  cursor: pointer;
}
</style>