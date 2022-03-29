<template>
    <h1>PLAY TEXT</h1>
        <section>
          <div id="read_List">
              <h1>{{textInDisplay}}</h1>
          </div>
          <button @click="textStart();">PLAY</button>
          <button @click="textStop();">PAUSE</button> 
        </section>
</template>

<script>
export default {
    name: 'PlayText',
    data() {
      return {
          text: "I can't believe the news today. Oh I can't close my eyes and make it go away",
          word:"",
          timeInterval: 5000,
          textByWords:[],
      }
    },
    mounted() {
         this.loadData();
        
    },
    methods: { 
        textInDisplay(word){
            this.textByWords = this.text.split(" ");
            if(word >= this.textByWords.length -1){
                clearInterval()
            }else{
                word++;
            }
        },   
    textStart(setInterval(() => {
        
    }, timeinterval)) 

    textStop(clearInterval) 
    },
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
</style>

    