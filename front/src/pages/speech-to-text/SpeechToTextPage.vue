<!-- <template>
  <h1>amigo lector</h1>
	<div class="app">
		<button :class="`mic`" @click="ToggleMic">di lo que te salga del horno</button>
		<div class="transcript" v-text="transcript"></div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
const transcript = ref('')
const isRecording = ref(false)
const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition
const sr = new Recognition()
onMounted(() => {
	sr.continuous = true
	sr.interimResults = true
	sr.onstart = () => {
		console.log('SR Started')
		isRecording.value = true
	}
	sr.onend = () => {
		console.log('SR Stopped')
		isRecording.value = false
	}
	sr.onresult = (evt) => {
		for (let i = 0; i < evt.results.length; i++) {
			const result = evt.results[i]
			if (result.isFinal) CheckForCommand(result)
		}
		const t = Array.from(evt.results)
			.map(result => result[0])
			.map(result => result.transcript)
			.join('')
		
		transcript.value = t
	}
})
const CheckForCommand = (result) => {
	const t = result[0].transcript;
	if (t.includes('stop recording')) {
		sr.stop()
	} else if (
		t.includes('what is the time') ||
		t.includes('what\'s the time')
	) {
		sr.stop()
		alert(new Date().toLocaleTimeString())
		setTimeout(() => sr.start(), 100)
	}
}
const ToggleMic = () => {
	if (isRecording.value) {
		sr.stop()
	} else {
		sr.start()
	}
}
</script>
<style>
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family:Arial, Helvetica, sans-serif;
}
body {
	background:white;
	color: black;
  font-size: 1.5em;
}
</style> -->
<template>
  <h1>amigo lector</h1>
  <label for="voces">Selecciona la voz:</label>
    <br>
   <select id="voces">
		</select>
		<br>
		<br>
		Escribe tu mensaje:<br>
		<textarea id="mensaje" cols="30" rows="5"></textarea>
		<br><br>
		<button id="btnEscuchar">Escuchar</button>
</template>

<script>
export default {
  name:"pepe",
  data(){
    return{
      voces:"",
      vocesDisponibles:[],
      idiomas_preferidos:[],
      posibleIndice:0,
      indice:[],
    }
  },


mounted(){
  this.loadData()
  // this.voiceChecked()
  this.cargarVoces()
},

computed:{
},

methods:{
    async loadData() {
        const response = await fetch('http://localhost:5000/api/activities/wordbyword')
        this.texts = await response.json()
    },
    // async voiceChecked(){
    //  if ('speechSynthesis' in window); 
    //  return alert("Lo siento, tu navegador no soporta esta tecnología");
    // },

    async cargarVoces() {
        if (this.vocesDisponibles.length > 0) {
          console.log("No se cargan las voces porque ya existen: ", this.vocesDisponibles);
          return;
        }
        this.vocesDisponibles = speechSynthesis.getVoices();
        console.log( this.vocesDisponibles )
        let posibleIndice = this.vocesDisponibles.findIndex(voz => this.idiomas_preferidos.includes(voz.lang));
        if (posibleIndice === -1) posibleIndice = 0;

        this.vocesDisponibles.forEach((voz, indice) => {
              const opcion = document.createElement("option");
              opcion.value = indice;
              opcion.innerHTML = voz.name;
              opcion.selected = indice === posibleIndice;
              this.$voces.appendChild(opcion);
        });
    }
  }
}
</script>

<style>
body {
  text-align: center;
}
</style>