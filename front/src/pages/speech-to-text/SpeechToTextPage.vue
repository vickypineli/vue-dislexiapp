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
      IDIOMAS_PREFERIDOS:["eu-ES", "en-GB", "es-ES"],
      posibleIndice:0,
    }
  },


mounted(){
  this.loadData()
  this.cargarVoces()
},
computed:{
  voiceChecked(){
     if ('speechSynthesis' in window); 
     return alert("Lo siento, tu navegador no soporta esta tecnología");
  }

},
methods:{
    async loadData() {
        const response = await fetch('http://localhost:5000/api/activities/wordbyword')
        this.texts = await response.json()
    },

    async cargarVoces() {
        if (this.vocesDisponibles.length > 0) {
          console.log("No se cargan las voces porque ya existen: ", this.vocesDisponibles);
          return;
        }
        this.vocesDisponibles = speechSynthesis.getVoices();
        console.log( this.vocesDisponibles )
        let posibleIndice = this.vocesDisponibles.findIndex(voz => this.IDIOMAS_PREFERIDOS.includes(voz.lang));
        if (posibleIndice === -1) posibleIndice = 0;
        this.vocesDisponibles.forEach((voz, indice) => {
          const opcion = document.createElement("option");
          opcion.value = indice;
          opcion.innerHTML = voz.name;
          opcion.selected = indice === posibleIndice;
          this.$voces.appendChild(opcion);
        });
        // Si no existe la API, lo indicamos
    }
  }
}
</script>

<style>
body {
  text-align: center;
}
</style>