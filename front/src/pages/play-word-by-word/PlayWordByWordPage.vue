<template>
    <h1>PLAY TEXT</h1>
        <section>
          <div id="read_List">
              <h1>{{textArray}}</h1>
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
          text: "",
          timeInterval: 5000,
          textArray:[],
      }
    },
    mounted() {
         this.loadData()
         this.showLocaleTime()
    },
    methods() { 
        converTextToArray() {
            this.text = "I can't believe the news today. Oh I can't close my eyes and make it go away";
            this.textArray  = this.text.split(" ");
            console.log(textArray);
            return
        }

        textStart(){
            setInterval(converTextToArray), this.timeInterval)
        }

        textStop(){
            clearInterval()
        }
        
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
</style>

    