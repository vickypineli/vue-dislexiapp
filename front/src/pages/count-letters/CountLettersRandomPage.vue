<template>

    <section class="container">
        <h1>SILABAK ZENBATU</h1>
        <article class="exerxice-box" v-for="word in words" :key="word.id">
            <div class="title-area">          
                <p>{{ word.word }}</p>
            </div>
            <div class="question-area">
                <div class="draw">
                    <img class="photo" :src="word.img" />
                </div>
                <div class="answers">
                    <div class="inputs-box">
                        <label for="letters" >- Zenbat letrak? </label>
                        <input type="text" v-model="word.inputnumberletters">
                    </div>
                    <div class="inputs-box">
                        <label for="syllables">- Zenbat silabak? </label>
                        <input type="text" v-model = "word.inputnumbersyllables">   
                    </div>
                </div>
                <div class="solutions">
                        <div v-if="word.inputnumberletters == null"></div>
                        <div v-else-if="word.inputnumberletters == word.letters">🎉 Ondo.</div>
                        <div v-else>❌{{word.letters}} letrak.</div>
                        <div v-if="word.inputnumbersyllables == null"></div>
                        <div v-else-if="word.inputnumbersyllables == word.syllables">🎉 Ondo.</div>
                        <div v-else>❌{{word.syllables}} silabak .</div>
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
                <button  class="buttonstart" @click="this.loadData"> JOLASTU BERRIRO
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
.container {
    width: 90vw;
    margin: auto;
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    
}
.exerxice-box{
    width: 550px;
    height: 200px;
    margin: 0.8vw;
    display: flex;
    flex-direction: column;
    border: 4px dashed #42b983;
    border-radius: 15px;
    align-items: center;
}
.question-area{
    display: flex;
    flex-direction: row;
  
}
.title-area{
    widows: 500px;
    height: 70px;
    font-size: 25px;
    text-transform: uppercase;
    font-weight: bold;
    color: rgb(255, 0, 85);
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.draw {
    width: 180px;
    height: 120px;
}
.photo {
    width: 110px;
    height: 110px;
    margin: auto;
}
.answers {
    width: 210px;
    height: 120px;
    display: flex;
    flex-direction: column;
    align-content: center;

}
.inputs-box{
    text-align: center;
    display: flex;
    flex-direction: row;
    align-items: baseline;
}
.solutions {
    width: 110px;
    height: 120px;
    display: flex;
    flex-direction: column;
    align-items: baseline;
    padding: 5px;
    justify-content: space-between;
    font-size: 20px;
    
}
.text{
    font-size: 1.5em;
    padding: 15px;
}
label{
    width: 190px;
    height: 60px;
    font-size: 1.3em;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
input{
    align-content: center;
    font-size: 1.7em;
    text-align: center;
    width: 40px;
    height: 40px;
    border: 1px solid rgb(255, 0, 85);
    border-radius: 5px;
   
}
h1 {
  width: 90vw;
  height: 40px;
  margin: auto;
  font-size:2.0em ;
  font-family: 'Slackey';
  text-transform: uppercase;
  color: rgb(242, 117, 8);
}

.finish-game-container{
    width: 85vw;
    height: 10vh;
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    background: #42b983;
    color: white;
    border-radius: 15px;
}
.buttonfinish {
    margin: 10px;
    padding: 5px 10px;
    border-color:rgb(145, 144, 144);
    border-radius: 15px;
    font-size: 1.2em;
    background: #42b983;
   
}
.buttonstart {
    margin: 10px;
    padding: 5px 10px;
    border-color:rgb(255, 0, 85);
    border-radius: 15px;
    font-size: 1.2em;
    font-weight: bold;
    background: white;
    color:#42b983;
    color:rgb(247, 9, 88);
}

</style>