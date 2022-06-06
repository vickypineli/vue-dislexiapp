<template>
  <h1>SILABAK ZENBATU</h1>
    <section class="word-item" v-for="word in words" :key="word.id">
        <article class="draw">
            <img class="photo" :src="word.img" />
        </article>

        <article class="question-container">
            <h2>{{ word.word }}</h2>
            <div class="question">
                <label for="letters" >Zenbat letrak? </label>
                <input type="text" :value="lettersnumber" > 
                <div v-if="answercorrectletters == true">🎉🏆</div>
                <div v-else>❌{{word.letters}}</div>
            </div>            
            <div class="question">
                <label for="syllables">Zenbat silabak? </label>
                <input type="text" v-model="syllablesnumber"> 
                <div v-if="answercorrectsyllables == true">🎉🏆</div>
                <div v-else>❌{{word.syllables}}</div>
            </div>
            
        </article>

    </section>
    <div class="finish-game-container" >
        <div class="text">{{text}}</div>
        <button @click="finish = !finish" :class="styles">
            <div v-if="!finish">HASI</div>
            <div v-else>EMAITZAK</div>
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
            text: "Amaitu duzu ariketa?",
            lettersnumber:0,
            syllablesnumber:0,
            answercorrectletters: true,
            answercorrectsyllables: true,
        }
    },
    watch:{
        finish(value){
            if(value){
                this.text ="Amaitu duzu ariketa?";
                    return this.loadData();           
            } else {
                this.text= "Nahi baduzu jolastu berriro?"
                    return this.results();
            }
        }
    },

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
        results(){
            console.log("click")
            // if (this.lettersnumber == this.word.letters || this.syllablesnumber == this.word.syllables) {
            //     this.correctanswer = true;
            // }else{
            //     this.correctanswer = false;
            // }
        }
    },
    computed: {
        styles(){
            return this.finish ? ['buttonstart'] : ['buttonfinish'];
        }
    },
};

</script>

<style scoped>
body{
  background-image: url("https://i.ibb.co/MhBFzhC/paisaje.png");
}
.photo {
    width: 200px; 
    margin-inline: 20px;
}

h2 {
    font-size: 1.5em;
    text-transform: uppercase;
}
.word-item{
    display: flex;
    flex-direction: row;
    border: 1px solid green;
    border-radius: 15px;
    padding: 0px, 10px;
    width: 90vw;
    margin:0px;
}
.draw {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 50vw;
}
.question-container {
    display: flex;
    flex-direction: column;
    width: 30vw;
}
.question {
    margin: 10px;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
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
    font-size: 2.1em;
    height: 5vh;
    border: 2px solid red;
    border-radius: 50px;
    width: 5vw;
}
</style>