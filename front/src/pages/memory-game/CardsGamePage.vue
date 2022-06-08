<template>
  <div id="app">
  <p> pairs: {{pairs}} / 50</P>

  <ul class="images">
    <li v-for="image, i in images" v-bind:key="image + i" v-bind:class="image" v-on:click="select">{{image}}</li>
  </ul>

</div>
</template>

<script>
new Vue({
  el: "#app",
  data: {
    activeImage: "",
    pair: "",
    pairs: 0,
    images: [
      "🌈",
      "☔️",
      "🐹",
      "🎺",
      "🐬",
      "🦚",
      "🦧",
      "🕸",
      "🦩",
      "🐠",
      "🐓",
      "🍄",
      "🌻",
      "🌞",
      "🐿",
      "🌏",
      "🌝",
      "❄️",
      "🌹",
      "☃️",
      "🍇",
      "🍓",
      "🍈",
      "🥑",
      "🥦",
      "🍞",
      "🥔",
      "🍗",
      "🌮",
      "🥃",
      "🏓",
      "🏵",
      "🎹",
      "🦨",
      "☠️",
      "🤡",
      "💩",
      "🤯",
      "😱",
      "🥰",
      "🎃",
      "🤖",
      "😻",
      "🚗",
      "✈️",
      "🚀",
      "🏜",
      "🎆",
      "💾",
      "⏰"
    ]
      .flatMap((i) => [i, i])
      .sort(() => Math.random() - 0.5)
  },
  methods: {
    select: function (event) {
      // show selected card
      event.target.classList.add("active");
      // fill in both variables
      this.activeImage == ""
        ? (this.activeImage = event.target.innerHTML)
        : (this.pair = event.target.innerHTML);

      // see the other selected card and then remove active class
      var unpaired = Array.from(document.getElementsByTagName("li"));
      this.activeImage != "" &&
        this.pair != "" &&
        setTimeout(() => {
          unpaired.map((item) => item.classList.remove("active"));
        }, 1000);

      // compare variables
      if (
        this.activeImage != "" &&
        this.pair != "" &&
        this.activeImage == this.pair
      ) {
        this.pairs = this.pairs + 1;
        var matches = Array.from(
          document.getElementsByClassName(this.activeImage)
        );
        matches.map((pairItem) => pairItem.classList.add("paired"));
        console.log(matches, this.activeImage);
        this.activeImage = "";
        this.pair = "";
      } else if (
        this.activeImage != "" &&
        this.pair != "" &&
        this.activeImage != this.pair
      ) {
        this.activeImage = "";
        this.pair = "";
      }
    }
  }
});

</script>

<style>
html {
  background: #222;
  user-select: none;
  p {
    color: white;
    font-family: verdana;
    width: 100%;
    text-align: center;
  }
  ul {
    display: flex;
    margin: 1rem;
    flex-flow: wrap;
    width: 95%;
    max-width: 1100px;
    height: 90vh;
    margin: 1rem auto;
    padding: 0;
    justify-content: space-around;
    li {
      background: #333;
      box-shadow: 2px 2px 5px 0px rgba(0, 0, 0, 0.5);
      width: 10%;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 2rem;
      width: 8%;
      height: 8%;
      margin: 1%;
      border-radius: 0.75rem;
      box-sizing: border-box;
      color: transparent;
    }
    .active {
      background: #555;
      pointer-events: none;
      color: unset;
    }
    .paired {
      background: #777;
      color: unset;
      pointer-events: none;
    }
  }
}
</style>