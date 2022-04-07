<template>
  <h1>HITZEZ HITZ</h1>
  <section id="container">
  <article class="text">
        <select v-model="textSelected">
        <option v-for="text in texts" :key="text" :value="text.text">
          {{ text.language }}
        </option>
      </select>
  </article>
  <br>
<textarea v-model="textSelected" placeholder="add multiple lines"></textarea>
  <article class="language">
    <input
      type="radio"
      id="Basque-text"
      value="euskera"
      v-model="languageSelected"
    />
    <label for="">Inglesa</label>

    <input
      type="radio"
      id="english-text"
      value="ingesela"
      v-model="languageSelected"
    />
    <label for="">Euskera</label>

    <input
      type="radio"
      id="spanish-text"
      :value="gastelania"
      v-model="languageSelected"
    />
    <label for="">Gaztelania</label>
    <br />
    <span>{{ languageSelected }}</span>
    <br />
  </article>
  <article class="speed">
    <label>Hitz-minuturo</label>
    <input v-model="wordsByMinute" type="number" min="30" max="100" />
    <br />
    <span> {{ wordsperminute }}</span>
    <article>
      <br />
    </article>
    <label>Letra-tipo</label>
    <select v-model="fontSelected">
      <option disabled value="letra-tipo">Select</option>
      <option  @click="open = !open" value="arial"> Arial</option>
      <option value="escolar" >Escolar</option>
      <option value="dislexia" >Dislexia</option>
    </select>
    <br />
    <span> {{ fontSelected }}</span>
  </article>
  <article>
    <label for="checkbox">Entzun: {{ voiceSelected }}</label>
    <input
      type="checkbox"
      id="checkbox"
      true-value="BAI"
      false-value="EZ"
      v-model="voiceSelected"
    />
  </article>
  <article>
    <input type="submit" value="Datuak gorde" />
  </article>
  </section>
 
  <router-link to="/activities/word-by-word/play-word-by-word"
    ><button>GOAZEN IRAKURTZERA..!!</button></router-link>
</template>"
<script>
export default {
  name:"WordByWord",
    data(){
        return{
          languageSelected:'',
          fontSelected:'',
          wordsByMinute:'',
          voiceSelected:'',
          texts:[],
          textSelected:"",
        }
    },
    mounted(){
      this.loadData()
    },
    methods:{
      async loadData() {
        const response = await fetch('http://localhost:5000/api/activities/wordbyword')
        this.texts = await response.json()
      },
    }    
}
</script>

<style scoped>
#container{
  margin: auto;
}
textarea {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  width: 80vw;
  height: 10vh;
}
style-font-arial{
  font-family: Arial, Helvetica, sans-serif;
}
style-font-arial{
  font-family: 'Times New Roman', Times, serif;
}
style-font-arial{
  font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
}
article {
  padding: 0.7em;
}

</style>