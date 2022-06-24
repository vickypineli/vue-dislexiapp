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
          <p>( Zailena Maila)</p>
        </div>
    </section>
    <section class="exercise-box" v-for="phrase in phrases" :key="phrase.id">
        <article class="draw-area">
            <img class="photo" :src="phrase.img"/>
        </article>
        <article class="question-area">
            <p class="question">{{phrase.question}}</p>
            <input class="answer" type="text" v-model="phrase.inputanswer"/>
            
            <div class="solution">
            <div>
                <p v-show = "solutionGood === true">🎉Oso ondo egin duzu....!!</p>
                <p v-show = "solutionBad ===true">❌Saiatu berriro.</p>
            </div>
            <button  class="buttonfinish" @click="result"> EMAITZA</button>

        </div>
        </article>
    </section>
    
    <section>    
        <div class="finish-game-container" >
          <div class="text">{{text}}</div>
            <!-- <button @click="finish = !finish" :class="styles">
                    <div v-if="!finish">GOAZEN</div>
                    <div v-else>EMAITZA</div>
            </button> -->
            <button  class="buttonstart" @click="playAgain()"> JOLASTU BERRIRO</button> 
        
        </div>
        
    
    </section>
</div>
</template>
<script>
export default {
    name:"ChainedWord",
    data() {
            return {
                finish: false,
                text:"Amaitu duzu ariketa?",
                phrases:[], 
                phrase:"",
                solutionGood: false,
                solutionBad: false,
               
            }
    },
    // watch:{
    //     finish(value){
    //         if(value){
    //             this.result(); 
    //         } else {
    //             this.text ="Nahi baduzu jolastu berriro?";
    //             this.loadData();
    //         }
    //     }
    // },
    mounted(){
        this.loadData();
    },

    methods: {
        async loadData() {
            const response = await fetch("http://localhost:5000/api/activities/chainedword/hard");
            this.phrases = await response.json();
        },
        playAgain(){
                this.solutionGood = false;
                this.solutionBad = false;
                this.loadData();
            
        },
        result() {
    
                if (this.phrases[0].inputanswer === this.phrases[0].answer) {
                 
                    this.solutionGood = true; 
                    this.solutionBad = false;  
                } else {
                    this.solutionGood = false;  
                    this.solutionBad = true;
                }
        }
    },
    // computed: {
    //     styles(){ 
    //             return this.finish ? ['buttonstart'] : ['buttonfinish'];
    //             }
    // }
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
.exercise-box{
    width: 90vw;
    height: 30vh;
    display: flex;
    justify-content: center;
    border: 4px dashed #42b983;
    border-radius: 15px;
}

.question-area{
    display:flex;
    flex-direction: column;
}
.question{
    width: 60vw;
    margin: auto;
    margin-top: 10px;
    font-size: 2.2vw;
    text-align: center;
    font-weight: bold;
    color: rgb(255, 0, 85);
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; 
}
.answer{
    width:50vw;
    margin: auto;
    margin-top: 20px;
    font-size: 1em;
    text-align: center;
    font-weight: bold;
    color: rgb(71, 69, 69);
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; 
}
.text{
    font-size: 1.3em;
}
.photo{
    width: 150px;
    height: 150px;
}
.solution{
    width: 60vw;
}
.finish-game-container{
    width: 80vw;
    display:flex;
    margin-top:  10px;
    justify-content: space-evenly;
    align-items: baseline;
    background: rgba(98, 233, 188, 0.164);
}
.buttonfinish {
    width: 40vw;
    margin: 10px;
    padding: 0px 10px;
    border-color:rgb(145, 144, 144);
    border-radius: 15px;
    font-size: 1.2em;
    background: rgb(255, 0, 85);
    color: white;
}
.buttonstart {
    width: 30vw;
    height: 10vh;
    margin: 10px;
    padding: 0px 10px;
    border-color:rgb(255, 0, 85);
    border-radius: 15px;
    font-size: 1.2em;
    background: white;
    color:rgb(255, 0, 85);
}

button {
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
  height: 80px;
  margin: auto;
  margin-top: 4vh;
  font-size:5vw ;
  font-family: 'Slackey';
  text-transform: uppercase;
  color: rgb(242, 117, 8);
}

</style>