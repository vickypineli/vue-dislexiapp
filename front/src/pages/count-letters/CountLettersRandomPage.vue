<template>
  <h1>SILABAK ZENBATU</h1>
    <section class="exercises-container">
        <article class="question-box" v-for="word in words" :key="word.id">
            <div class="draw-area">
                <div class="title">
                    <h2>{{ word.word }}</h2>
                </div>
                <img class="photo" :src="word.img" />
            </div>
            <div class="questions-area">

                <div class="answers" >
                    <label for="letters" >Zenbat letrak? </label>
                    <input type="text" v-model="word.inputnumberletters"> 

                    <label for="syllables">Zenbat silabak? </label>
                    <input type="text" v-model = "word.inputnumbersyllables">
                </div>            
                <div class="solutions">
                    <div v-if="word.inputnumbersyllables == null"></div>
                    <div v-else-if="word.inputnumbersyllables == word.syllables">🎉</div>
                    <div v-else>❌{{word.syllables}} silabak .</div>
                    
                    <div v-if="word.inputnumberletters == null"></div>
                    <div v-else-if="word.inputnumberletters == word.letters">🎉</div>
                    <div v-else>❌{{word.letters}} letrak.</div>
                </div>
            </div>
        </article>
            <div>
                <!-- <div v-show ="resultOfExercise == true">SUPER ONDO🎉</div>
                <div v-show ="resultOfExercise == false">TXARTO❌</div>
                <button @click="results">EMAITZAK</button> -->
            </div>

      
    </section>
            <div class="finish-game-container" >
                <div class="text">{{text}}</div>
                <button @click="this.loadData"> JOLASTU BERRIRO
                <!-- <button @click="finish = !finish" :class="styles">
                    <div v-if="!finish">HASI</div>
                    <div v-else>BAI</div> -->
                </button>
            </div> 
</template>

<script>

export default {
    name: "CountlettersRandom",
    
    data() {
        return {
            words:[], 
            finish: true,
            text: 'Amaitu duzu ariketa?',
            resultOfExercise: '',
        }
    },
    // watch:{
    //     finish(value){
    //         if(value){
    //             this.text ="Amaitu duzu ariketa?";
    //                 return this.loadData();           
    //         } else {
    //             this.text= "Nahi baduzu jolastu berriro?"
    //                 return this.results();
    //         }
    //     }
    // },

    mounted() {
        this.loadData();
    },

    methods: {
        async loadData() {
        const response = await fetch(
            "http://localhost:5000/api/activities/countlettersrandom"
        );
        this.words = await response.json();
        },

        // resultquestionofsyllables () {
        //     if (this.word.inputnumbersyllables == this.word.syllables) {
        //         this.resultnumbersyllables == true
        //     } else {
        //         this.resultnumbersyllables == false
        //     }
        // },
        // resultquestionofletters () {
        //     if (this.word.inputnumberletters == this.word.letters) {
        //         this.resultnumberletters == true
        //     } else {
        //         this.resultnumberletters == false
        //     }
        // },
        // results(){
        //     if (this.resultnumbersyllables == true && this.resultnumberletters == false){
        //         this.resultOfExercise = false;
        //     } else if (this.resultnumbersyllables == false && this.resultnumberletters == true) { 
        //         this.resultOfExercise = false; 
        //     } else if (this.resultnumbersyllables == false && this.resultnumberletters == false) { 
        //         this.resultOfExercise = false;     
        //     } else {
        //         this.resultOfExercise = true;  
        //     }
        // }
    },
    // computed: {
    //     styles(){
    //         return this.finish ? ['buttonstart'] : ['buttonfinish'];
    //     }
    // },
};

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Slackey&display=swap');
.exercises-container {
    width: 90vw;
    height: 60vh;
    margin: auto;
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    align-content: space-around;
}
.question-box{
    width: 40vw;
    height: 25vh;
    margin: 0.5em;
    display: flex;
    flex-direction: row;
    border: 2px dashed green;
    border-radius: 15px;
    align-items: center;
}
.draw-area {
    width: 20vw;
    height: 20vh;
    margin:5px;
    display: flex;
    flex-direction: column;
    justify-items: center;
    border: 2px dashed red;  
}
.photo {
    width: 15vw;
    height: 15vh;
    text-align: center;
}
.questions-area{
    width: 30vw;
    height: 20vh;
    margin:5px;
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 2px solid red;
}
.title {
    width: 20vw;
    height: 4vh;
    background: #5dfdb5;
    font-size: 0.5em;
    text-transform: uppercase;
    color: green;
}
.answers {
    width: 20vw;
    height: 10vh;
    display: flex;
    flex-direction: row;
    justify-content: center;
    background: #5df2fd;
    border: 2px dashed red;
}
.solutions {
    width: 20vw;
    height: 6vh;
    display: flex;
    flex-direction: row;
    justify-content: center;
    background: #fd5dfd;
    border: 2px solid blue;
}

h1 {
  width: 90vw;
  margin: auto;
  font-style: italic;
  font-family: 'Slackey';
  font-size: 2.5em;
  text-transform: uppercase;
  color: rgb(242, 117, 8);
}

.finish-game-container{
    margin: 10px;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
}
.buttonfinish {
    margin: 10px;
    padding: 5px 10px;
    border-color:gray;
    border-radius: 15px;
    font-size: 1.2em;
    background: #42b983;
    color:white;
}
.buttonstart {
    margin: 10px;
    padding: 5px 10px;
    border-color:#42b983;
    border-radius: 15px;
    font-size: 1.2em;
    background: white;
    color:#42b983;
}
.text{
    font-size: 1.5em;
    padding: 15px;
}
input{
    text-align: center;
    font-size: 1.2em;
    width: 4vw;
    height: 4vh;
    border: 1px solid rgb(0, 34, 255);
    border-radius: 50px;
}
</style>