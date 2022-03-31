<template>
    <h1>PLAY TEXT</h1>
        <section id="container" :class="styles">
            <div>
                <h1>{{text.split(" ")}}</h1>
                <div v-if= "play">
                    <h1>{{word}}</h1>
                </div>
                <button @click="play = !play">
                  <div v-if ="!play"> PLAY </div>
                  <div v-else> PAUSE </div> 
                </button>
            </div>
        </section>
</template>

<script>
export default {
    name: 'PlayText',
    data() {
        return {
            text: "I can't believe the news today. Oh I can't close my eyes and make it go away",
            word:" ",
            timeInterval: 7 * 1000,
            textByWords:[],
            play: false,
            label:"",
        
        }
    },
    mounted() {
            this.loadData();
            this.textInDisplay();

    },
    methods: { 
        async loadData() {
            const response = await fetch('http:localhost:5000/api/activities/wordbyword')
            this.texts = await response.json()
            console.table(response);
        },
        textInDisplay(){
            this.textByWords = this.text.split(" ");
                if(this.word >= this.textByWords.length-1){
                    clearInterval()
                }else{
                    this.word++;
                }
        },   
    // watch:{
    //     play(value){
    //         if(value){
    //             this.textStart(setInterval(this.timeInterval))
    //         }else{
    //             this.textStop(clearInterval)
    //         }
    //     }
    // }, 
    // computed: {
    //     label() {
    //         return this.play ? "PAUSE" : "PLAY";
    //             }
    //     }    
    }
}

</script>

<style>
body {
      text-align: center;
    }
    section{
      margin: 1.5em;
      border: 0.3em solid red;
      padding: 1.5em;
    }
    button{
        color:blue;
        font-size: 1.5em;
    }
    h1{
        color:green;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;

    }
</style>

    