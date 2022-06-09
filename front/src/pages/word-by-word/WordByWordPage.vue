<template>
  <div class="container">
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
        <label> Testua: </label>
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
        <option value="150"></option>
        </datalist>
      </div>
    
    </section>  
      <textarea
        v-model="textSelected"
        placeholder="Aldatu testua hemen....."
        :style="fontSelected"
      ></textarea>
  </div>  
</template>

<script>
export default {
  name: "Word-by-word",
  data() {
    return {
      word: "",
      wordsByMinute: 10,
      textByWords: [],
     
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
      return 60000 / this.wordsByMinute;
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
      console.log ("clearInterval", this.play)
      this.pause = clearInterval(this.play);
    },

    PlayText() {
      this.textByWords = this.textSelected.split(" ");
      let item = 0;
      this.play = setInterval(() => {
        this.word = this.textByWords[item];
        item += 1;
      }, this.timeInterval);
      console.log ("setInterval", this.play) 
        
      
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Slackey&display=swap");


.text-container {
  margin: auto;
  display: flex;
  width: 80vw;
  height: 25vh;
  background: white;
  border: 1.5px solid rgb(3, 97, 3);
  border-radius: 10px;
}
.text{
  flex: auto;
  font-size: 3em;
  margin: auto;
}

button{
  display: block;
  font-size: 20px;
  padding: 8px;
  margin: 20px;
  border-radius: 15px;
  border-color: rgb(41, 194, 41);
  background: rgb(34, 185, 34);
  color:white;
}
.options {
  /* margin-top: 10px; */
  /* margin-bottom: 20px; */
  width: 80vw;
  display: flex;
  margin: auto;
  flex-direction: row;
}
.option-item{
  display: flex;
  flex-direction: column;
  width: 25vw;
  margin: 15px;
}
.range{
  margin: 5px;
}
textarea {
  font-size: 1.3em;
  border-radius: 10px;
  border-color: darkgreen;
  width: 80vw;
  height: 15vh;
  background: rgba(255, 255, 255, 0.73);
}
label{
  margin: 5px;
  font-size: 1.2em;
}
select {
  font-size: 1.2em;
}
.slider {
  -webkit-appearance: none;  /* Override default CSS styles */
  appearance: none;
  width: 100%; /* Full-width */
  height: 10px; /* Specified height */
  background:rgb(146, 148, 146); /* Grey background */
  outline: none; /*Remove outline  */
  opacity: 0.7; /* Set transparency (for mouse-over effects on hover) */
  -webkit-transition: .2s; /* 0.2 seconds transition on hover */
  transition: opacity .2s;
}
.slider:hover {
  opacity: 1; /* Fully shown on mouse-over */
}
/* The slider handle (use -webkit- (Chrome, Opera, Safari, Edge) and -moz- (Firefox) to override default look) */
.slider::-webkit-slider-thumb {
  -webkit-appearance: none; /* Override default look */
  appearance: none;
  width: 15px; /* Set a specific slider handle width */
  height: 25px; /* Slider handle height */
  background: darkgreen; /* Green background */
  cursor: pointer; /* Cursor on hover */
}

.slider::-moz-range-thumb {
  width: 25px; /* Set a specific slider handle width */
  height: 25px; /* Slider handle height */
  background: darkgreen; /* Green background */
  cursor: pointer; /* Cursor on hover */
}
</style>