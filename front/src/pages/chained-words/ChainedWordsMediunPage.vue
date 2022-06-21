<template>
<div class="container">
    <h1>HITZ KATEATUAK</h1>
    <section class="buttons-box">
        <div class="buttons">
            <router-link to="/activities/chained-words/easy"><button>ERRASA</button></router-link>
            <router-link to="/activities/chained-words/mediun"><button>NORMALA</button></router-link>
            <router-link to="/activities/chained-words/hard"><button>ZAILENA</button></router-link>
        </div>
        <div class="despcription">
          <p>( Ertaina Maila)</p>
        </div>
    </section>
    <section class="exerxice-area" v-for="phrase in phrases" :key="phrase.id">
        <p class="question">{{phrase.question}}</p>
        <input class="answer" type="text" v-model="phrase.inputanswer"/>
        <div class="solution">
            <div v-if="phrase.inputanswer == null"></div>
            <div v-else-if="phrase.inputanswer == word.answer">🎉 Ondo.</div>
            <div v-else >❌</div>
        </div>
    </section>
    <section>    
        <div class="finish-game-container" >
          <div class="text">{{text}}</div>
            <button @click="finish = !finish" :class="styles">
                    <div v-if="!finish">HASI</div>
                    <div v-else>EMAITZA</div>
            </button>
      </div>
    <!-- <button  class="buttonstart" @click="this.loadData"> JOLASTU BERRIRO</button>  -->
    </section>
</div>
</template>
<script>
export default {
  name:"ChainedWord",
  data() {
        return {
            finish:true,
            text:"Amaitu duzu ariketa?",
            phrases:[], 
        }
  },
  watch:{
    finish(value){
        if(value){
            this.text ="Amaitu duzu ariketa?";
                return this.loadData();           
            } else {
                this.text= "Nahi baduzu jolastu berriro?"
                return this.result();
            }
    }
  },
  mounted(){
    this.loadData();
  },

  methods: {
    async loadData() {
        const response = await fetch("http://localhost:5000/api/activities/chainedword/mediun");
        this.phrases = await response.json();
    }

  },
  computed: {
        styles(){
            return this.finish ? ['buttonstart'] : ['buttonfinish'];
        }
  },
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Slackey&display=swap");
.container {
    width: 90vw;
    height: 70vh;
    margin: auto;
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
}
.buttons-box{
    width: 80vw;
    height: 10vh;
    margin: 0.8vw;
    display: columns;
    align-items: center;
}
.buttons{
  display: flex;
  justify-content: space-around;
}
.exerxice-area{
    width: 80vw;
    height: 20vh;
    border: 4px dashed #42b983;
    border-radius: 15px;
}
.question{
    width: 70vw;
    margin: auto;
    margin-top: 20px;
    font-size: 2.8vw;
    text-transform: uppercase;
    text-align: center;
    font-weight: bold;
    color: rgb(255, 0, 85);
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; 
}
.answer{
    width:70vw;
    margin: auto;
    margin-top: 30px;
    font-size: 2vw;
    text-transform: uppercase;
    text-align: center;
    font-weight: bold;
    color: rgb(71, 69, 69);
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; 
}
.finish-game-container{
    width: 60vw;
    height: 10vh;
    display:flex;
    justify-content: space-evenly;
    align-items: baseline;
}
button{
    width:20vw;
    height: 4vh;
    padding: 0px 10px 0px 10px;
    border-color:rgb(145, 144, 144);
    border-radius: 10px;
    font-size: 1em;
    background: #42b983;
    color: white;
}
h1 {
  width: 90vw;
  height: 60px;
  margin: auto;
  margin-top: 4vh;
  font-size:5vw ;
  font-family: 'Slackey';
  text-transform: uppercase;
  color: rgb(242, 117, 8);
}

</style>