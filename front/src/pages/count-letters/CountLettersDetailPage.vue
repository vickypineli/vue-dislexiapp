<template>
  <h1>SILABAK ZENBATU</h1>
  <h3>word:{{word.id}}</h3>
    <p>{{word.word}}</p>
    <img class="photo" :src="word.img" />

</template>

<script>
import config from "@/config.js";

export default {
    name:"Count-letters",
    data() {
        return {
            word:{},
            
        };
    },
    mounted() {
        this.loadData();
    },
    methods: {
        async loadData() {
            // this.word ={
            //     id: "word_1",
            //     img: "https://i.ibb.co/KrTZs1M/klariona.png",
            //     letters: "8",
            //     syllables: "3",
            //     word: "klariona",
            //     }
        let wordId = this.$route.params.id;
        const response = await fetch(`${config.API_PATH}/activities/countletters/ ${wordId}`
        );
        this.word = await response.json();
        },
    },
}

</script>

<style scoped>
body{
  background-image: url("https://i.ibb.co/MhBFzhC/paisaje.png");
}
.photo {
    width: 200px; 
    margin-inline: 130px;
    padding: 10px;
}
p {
    font-size: 50px;
}
.word-item{
    display: flex;
    flex-direction: row;
    border: 1px solid green;
    border-radius: 15px;
    width: 90vw;
    margin:15px;
}
.draw {
    border: 1px solid red;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 70vw;
}
.question {
    display: flex;
    flex-direction: column;
    width: 30vw;
}
</style>