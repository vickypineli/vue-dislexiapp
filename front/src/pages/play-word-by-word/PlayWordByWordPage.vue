<template>
  <h1>IRAKURTZAILE</h1>
  <WordByWord @datos-guardados="save" />
  <section id="textreader">
    <button @click="StartText()">PLAY</button>
    <button @click="PauseText()">PAUSE</button>
    <div id="output">
      <h1>{{ word }}</h1>
    </div>
  </section>
</template>

<script>
import WordByWord from "../word-by-word/WordByWordPage.vue";
export default {
  name: "PlayText",
  components: { WordByWord },
  data() {
    return {
      text: "",
      word: "",
      timeInterval: 0,
      play: 0,
    };
  },
  mounted() {},

  computed: {
    SpeedCalculated() {
      let timeInterval = this.wordsperminute * 100; 
      return timeInterval
    },
  },
  methods: {
    save(value) {
      this.text = value;
    },
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
h1 {
  color: green;
  font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif;
}

#output {
  height: 2em;
  font-size: 3em;
}
</style>

    