<template>
    <h1>HITZEZ HITZ</h1>
<form>
      <article>
          <p>
            <label></label>
            <input type=radio name="text" v-model="textselected">Euskera
            <input type=radio name="text" v-model="textselected">Ingelesa
            <input type=radio name="text" v-model="textselected">Gaztelania
          </p>
          <!-- <textarea v-model="message" placeholder="add multiple lines"></textarea> -->
      </article>
      <article>
        <label>Hitz-minuturo</label>
        <input v-model="hitzminuturo" type="number" min="30" max="100">

        <label>Letra-tipo</label>
        <select v-model="fontseleted">
          <option disabled value="">Select</option>
          <option>Arial</option>
          <option>Escolar</option>
          <option>Dislexia</option>
        </select>
      </article>

      <article>
        <input type="checkbox" id="checkbox" v-model="voiceselected" />
        <label for="checkbox">Entzun:{{ voiceselected }}</label>
      </article>

      <article>
        <input type="submit" value="Datuak gorde">
      </article>
</form>
    <article>
      <ul>Hau da zure aukera:</ul>
          <li>{{"Testu: " + textselected}}</li>
          <li>{{"Letra: "  + fontseleted}}</li> 
          <li>{{"Hitz/m: " + hitzminuturo}}</li>
          <li>{{"Entzun: " + voiceselected}}</li>
    </article>
    <h2>{{texts}}</h2>
    <router-link to='/activities/word-by-word/play-word-by-word'><button>play</button></router-link>
</template>
<script>
export default {
    data(){
        return{
          textselected:'',
          fontselected:'',
          hitzminuturo:'',
          voiceselected:'',
          texts:{},
        };
    },
    mounted(){
      this.loadData()
    },
    methods:{
      async loadData() {
      const response = await fetch('http:localhost:5000/api/activities/word-by-word')
      this.texts = await response.json()
      
      }
    },
};
</script>

<style>
p{
  font-size: 1.5em;
}

li{
  text-align: left;
  margin-left:35.5px;
}
form{
  border: 0.5em solid gray;
  background: rgb(179, 176, 176);
}
label{
  padding: 1.2em;
}
</style>