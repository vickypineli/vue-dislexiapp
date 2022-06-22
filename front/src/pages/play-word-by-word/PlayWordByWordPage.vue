<template>
  <div>
    <h1>IRAKUR-LAGUN</h1>
  </div>    
  <section id="text">
        <label for="text">
          <textarea v-model="textSelected" placeholder="Jarri hemen zure testua....."></textarea>
        </label>
  </section>
  <section id="options-selec">
        <label>
          <select v-model="selectedVoice" >
          <option disabled >Aukeratu</option>
            <option v-for="(voice, index) in voices" :value="index" :key="index">
              {{ voice.name }}({{ voice.lang }})
            </option>
          </select>
        </label>
  </section>
  <section id="button-container" > 
        <button @click="play()"> PLAY </button>
        <button @click="stop()"> STOP </button>
        <button @click="pause()"> PAUSE </button>
  </section> 
   
     
        
</template>

<script>
export default {
  name:"Play-text",
  data(){
    return{
      texts: [],
      textSelected:"",
      langs: [],
      selectedLang:"",
      selectedVoice: 0,
      voices: [],
    }
  },
mounted(){
  this.loadData()
  this.loadVoicesList()
},
  
methods: {
  async loadData() {
        const response = await fetch('http://localhost:5000/api/activities/wordbyword')
        this.texts = await response.json()
    },
  async loadVoicesList() {
    if (
      typeof speechSynthesis !== "undefined" &&
      speechSynthesis.onvoiceschanged !== undefined
    ) {
      window.speechSynthesis.onvoiceschanged = () => this.onVoiceChanged();
    } else {
      this.onVoiceChanged();
    }
  },
  onVoiceChanged() {
      const voices = speechSynthesis.getVoices();
      this.$data.voices = voices;
      this.$data.selectedVoice = 0;
  },
  play() {
      const utterance = new SpeechSynthesisUtterance(this.textSelected);
      utterance.voice = this.$data.voices[this.$data.selectedVoice];
      speechSynthesis.speak(utterance);
  },
  stop() {
      speechSynthesis.cancel(this.utterance);
      },
  pause() {
      speechSynthesis.pause(this.utterance);
      },
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Slackey&display=swap');
h1 {
  width: 90vw;
  height: 40px;
  margin: auto;
  padding-top: 5%;
  font-size:2.0em ;
  font-family: 'Slackey';
  text-transform: uppercase;
  color: rgb(242, 117, 8);
}

textarea {
  margin: 10px;
  width: 90vw;
  height: 20vh;
  border: 4px dashed #42b983;
  border-radius: 15px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-size: 1.1em;
}

#options-selec {
  width: 70vw;
  margin: auto;
  padding: 20px;
  justify-content:space-around;
  display: flex;
}
#button-container {
    width: 95vw;
    height: 10vh;
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    border-radius: 15px;
}
button{
    width: 25vw;
    margin: 10px;
    padding: 0px 10px;
    border-color:rgb(170, 165, 167);
    border-radius: 15px;
    font-family: dislexia;
    font-size: 1.2em;
    font-weight: bold;
    background: #42b983;
    color:white; 
}
select {
  width: 80vw;
  height: 5vh;
  border: 2px solid rgb(255, 0, 85);
  border-radius: 5px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
   
}
</style>

    