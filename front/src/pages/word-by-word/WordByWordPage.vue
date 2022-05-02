<template>
  <div>
    <h1>HITZEZ-HITZ</h1>
  </div>
  <section class="text">
    <div>
      <h1 :style="fontSelected">{{ word }}</h1>
    </div>

  </section>
      <div>
      <button @click="PlayText()">PLAY</button>
      <button @click="PauseText()">STOP</button>
    </div>
  <section class="settings">
      <textarea v-model="textSelected" placeholder="Aukeratu testua....." :style="fontSelected"></textarea>
      <article >
        <select v-model="textSelected">
            <option disabled >Aukeratu testua</option>
            <option v-for="text in texts" :key="text" :value="text.text" >
              {{ text.language }}
            </option>
        </select>
        <select v-model="fontSelected">
          <option disabled >letra-tipo</option>
          <option :value="escolar" :style="escolar">ESCOLAR</option>
          <option :value="dislexia" :style="dislexia">DISLEXIA</option>
          <option :value="sarakanda" :style="sarakanda">SARAKANDA</option>
        </select>
            <label> Hitz-min. </label>
            <input v-model="wordsByMinute" type="number" min="10" max="90" />
      </article>
  </section>
</template>

<script>
export default {
  name: "Setting-Text",
  data() {
    return {
      text: "",
      word: "",
      wordsByMinute: 0,
      textByWords: [],
      play: 0,
      texts:[],
      textSelected:"",
      escolar: {
        fontFamily: 'escolar',
        color:'blue',
        },
      dislexia: {
        fontFamily: 'dislexia', 
        color:'green',
        },
      sarakanda: {
        fontFamily: 'sarakanda',
        color:'red',
        }
    };
  },
  computed:{
    timeInterval(){
      return this.wordsByMinute*100;
    }
  },
  mounted(){
    this.loadData()
  },
  methods: {
    async loadData() {
        const response = await fetch('http://localhost:5000/api/activities/wordbyword')
        this.texts = await response.json()
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
@import url('https://fonts.googleapis.com/css2?family=Slackey&display=swap');
@import url('/src/assets/fonts/escolar_N.TTF');
@import url('/src/assets/fonts/OpenDyslexic-Regular.otf');
@import url('/src/assets/fonts/sarakanda.ttf');
.text {
  margin: 10px;
  width: 80vw;
  height: 20vh;
  border: 0.4px double  #2c3e50;
  border-radius: 10px;
  padding: 1em;
  font-size: 2.5em;
}
textarea {
  font-size: 1.0em;
  border: 0.1px solid  #42b983;
  border-radius: 15px;
  width: 90vw;
  height: 10vh;
  font-family: 'escolar_N.TTF';
}
select {
  margin: 10px;
}
</style>