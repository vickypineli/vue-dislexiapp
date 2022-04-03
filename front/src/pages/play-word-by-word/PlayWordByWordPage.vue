<template>
  <h1>IRAKURTZAILE</h1>
  <section id="textreader">
      <div id="output" v-for="word in textByWords" :key="word">{{word}}</div>
      <br>
      <button @click="StartText();">PLAY</button>
      <button @click="PauseText();">PAUSE</button>
  </section>
  {{word}}
</template>

<script>
export default {
    name: 'PlayText',
    data() {
        return {
            text: "I can't believe the news today. Oh I can't close my eyes and make it go away",
            word:"",
            timeInterval: 1*1000,
            textByWords:[],
            play: null,
        }
    },
    mounted() {
        this.textInDisplay()
    },
    methods: { 
        textInDisplay(){
            this.textByWords = this.text.split(" ");                             
        },
        PauseText() {
            this.pause = clearInterval(this.play);
        },
        StartText(){
            this.play = setInterval(() =>{this.word++},this.timeInterval);
            {{this.word++}}
            if(this.word >= this.textByWords.length -1){       
                clearInterval(this.play);
            }else{
                this.word++; 
            }
        }
    }
};

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

    