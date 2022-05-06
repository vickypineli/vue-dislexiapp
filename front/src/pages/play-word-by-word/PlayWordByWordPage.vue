<template>
  <div>
    <h1>IRAKUR-LAGUN</h1>
  </div>    
  <section id="text">
        <label for="text">
          <textarea v-model="textSelected" placeholder="Testua....."></textarea>
        </label>
  </section>
  <section id="options-selec">
        <select v-model="textSelected">
          <option disabled >Aukeratu</option>
          <option v-for="text in texts" :key="text" :value="text.text" >{{ text.language }}</option>
        </select>
        <label>
          <select v-model="selectedVoice" >
            <option v-for="(voice, index) in voices" :value="index" :key="index">
              {{ voice.name }}({{ voice.lang }})
            </option>
          </select>
        </label>
  </section>
  <section id="btn-selector" > 
        <button @click="onButtonClick()"> PLAY </button>
        <button @click="stop()"> STOP </button>
        <button @click="pause()"> PAUSE </button>
        <button @click="resume()"> RESUME </button>
  </section>      
     
        
</template>

<script>
export default {
  name:"Play-text",
  data(){
    return{
      text:"",
      texts:[],
      textSelected:"",
      volumeSelected: 0,
      rateSelected: 0,
      pitchSelected: 0,
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
  onButtonClick() {
      // if (typeof speechSynthesis === "undefined") {
      //   this.$data.errorMessage = "speechSynthesis is undefined";
      //   return;
      // }
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
  resume() {
      speechSynthesis.resume(this.utterance);
      },
  }
};
</script>

<style>

textarea {
  margin: 10px;
  width: 90vw;
  height: 10vh;
  border: 0.3em double  #384d62;
  border-radius: 15px;
  font-family: sarakanda;
}
input[type='range']:focus {
  outline: none;
  color: red;
}
#options-selec {
  margin: 5px;
  padding: 15px;
  font-size: 1.1em;
 
}
#btn-selector {
  margin: 10px;
}
.rate .volume .pitch{
  margin: 10px;
}
</style>

    