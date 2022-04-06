<template>
  <h1>HITZEZ HITZ</h1>
  <article>
    <input
      type="radio"
      id="ingles"
      value="english_text"
      v-model="languageselected"
    />
    <label for="uno">Inglesa</label>

    <input
      type="radio"
      id="euskera"
      value="basque_text"
      v-model="languageselected"
    />
    <label for="Dos">Euskera</label>

    <input
      type="radio"
      id="text.text"
      value="spanish_text"
      v-model="languageselected"
    />
    <label for="Gazte">Gaztelania</label>
    <br />
    <span>{{ languageselected }}</span>
    <br />
  </article>
  <article>
    <label>Hitz-minuturo</label>
    <input v-model="wordsperminute" type="number" min="30" max="100" />
    <br />
    <span> {{ wordsperminute }}</span>
    <article>
      <br />
    </article>
    <label>Letra-tipo</label>
    <select v-model="fontselected">
      <option disabled value="letra-tipo">Select</option>
      <option value="arial">Arial</option>
      <option value="escolar">Escolar</option>
      <option value="dislexia">Dislexia</option>
    </select>
    <br />
    <span> {{ fontselected }}</span>
  </article>
  <article>
    <label for="checkbox">Entzun: {{ voiceselected }}</label>
    <input
      type="checkbox"
      id="checkbox"
      true-value="BAI"
      false-value="EZ"
      v-model="voiceselected"
    />
  </article>
  <article>
    <input type="submit" value="Datuak gorde" />
  </article>
  <article class="text-list">
    <li class="text-item" v-for="text in texts" :key="text">{{ text.text }}</li>
    <ul>
      <li class="text-item" v-for="(text, index) in texts" :key="index">
        {{ text.language }}
      </li>
    </ul>
  </article>
  <section class="textselect"> 
      <button v-for="(text, index) in texts" :key="index" @click="languageselected(index)">{{text.text}}</button>
      <button v-for="(text, index) in texts" :key="index" @click="languageselected(index)">{{text.language}}</button>
  </section> 

  <router-link to="/activities/word-by-word/play-word-by-word"
    ><button>GOAZEN IRAKURTZERA..!!</button></router-link
  >
</template>"
<script>
export default {
  name:"WordByWord",
    data(){
        return{
          languageselected:'',
          fontselected:'',
          wordsperminute:'',
          voiceselected:'',
          texts:[],
          textselected:"",
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
      // textselected(){
      //   this.texts.filter((text)=>text.language==this.languageselected)
      // }
    }    
}
</script>

<style>
p {
  font-size: 1.5em;
}

li {
  text-align: left;
  margin-left: 35.5px;
}
form {
  border: 0.5em solid gray;
  background: rgb(179, 176, 176);
}
label,
get-text {
  padding: 1em;
  font-size: 1.5em;
}
button,
input,
select,
span {
  font-size: 1.5em;
  color: green;
}
li {
  font-size: 1 em;
}
article {
  background: rgb(204, 243, 198);
}
.ingles {
  font-family: arial;
  color: blue;
}
.euskera {
  font-family: escolar;
  color: red;
}
.ingles {
  font-family: dislexia;
  color: green;
}
</style>