<template>
  <div :class="styles">
    <h1>IRAKURTZAILE</h1>
  </div>
  <section>
    <button @click="StartText()">PLAY</button>
    <button @click="PauseText()">STOP</button>  
    <div :class="styles">
      <h2>{{ word }}</h2>
    </div>
  </section>
    <button @click="open = !open">
          <div v-if="!open">IMPACT</div>
          <div v-else>impact</div>
    </button>

    <button @click="open = !open">
          <div v-if="!open">escolar</div>
          <div v-else>ESCOLAR</div>
    </button>
    <button :class="styles.segoe">segoe</button>
           
</template>

<script>
export default {
  name: "PlayText",
  data() {
    return {
      text: "I can't believe the news today. Oh I can't close my eyes and make it go away",
      word: "",
      wordsperminute:1000,
      textByWords: [],
      play: 0,
      open: true,
     
    };
  },
  mounted() {
   
  },
  watch: {
  open(value) {
      if (value) {
          return this.word;
      } else {
          return this.word;
      }
    }
  },
  computed:{
    timeInterval(){
      return this.wordsperminute;
    },
    styles(){
      return this.open ? ['open'] : ['close'] ;
    },
  },
  methods: {
    PauseText() {
      this.pause = clearInterval(this.play);
    },
    StartText() {
      this.textByWords = this.text.split(" ");
      let item = 0;
      this.play = setInterval(() => {
      this.word = this.textByWords[item];
      item += 1;
          }, this.timeInterval);
    },
  },
};
</script>

<style>
body {
  text-align: center;
}
section {
  margin: 1.5em;
  border: 0.3em solid red;
  padding: 1.5em;
}
button {
  color: blue;
  font-size: 1.5em;
}
#output{
    height: 2em;
    font-size: 3em;
}
button {
  margin: 24px;
  background-color: white;
  padding: 8px 24px;
  border-radius: 10px;
}
.close {
  font-family:BlinkMacSystemFont, Oxygen, Ubuntu, Cantarell;
 
}
.open {
  font-family:Impact;
   
}
.segoe {
font-family:'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif
}
.impact {
font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
}
.arial {
font-family: Arial, Helvetica, sans-serif;
}
</style>

    