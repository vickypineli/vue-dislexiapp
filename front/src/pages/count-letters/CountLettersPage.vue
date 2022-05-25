<template>
  <h1>SILABAK ZENBATU</h1>
    <article class="word-item" v-for="word in words" :key="word.id">
        <div class="draw">
            <img class="photo" :src="word.img" />
            <h2>{{ word.word }}</h2>
        </div>
        <div class="question">
            <label for="">Zenbat letrak? </label>
            <input type="number" min="1" max="20">
            <label for="">Zenbat silabak? </label>
            <input type="number" min="1" max="10">
        </div>
    </article>

</template>

<script>
export default {
    name:"Count-letters",
    data() {
        return {
            words:[],
        };
    },
    mounted() {
        this.loadData();
    },
    methods: {
        async loadData() {
        const response = await fetch(
            "http://localhost:5000/api/activities/countletters"
        );
        this.words = await response.json();
        },
    },
};
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