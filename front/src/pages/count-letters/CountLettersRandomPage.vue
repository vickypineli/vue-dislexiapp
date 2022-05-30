<template>
  <h1>SILABAK ZENBATU</h1>
    <section class="word-item" v-for="word in words" :key="word.id">
        <article class="draw">
            <img class="photo" :src="word.img" />
            
        </article>
        <article class="question-container">
            <h2>{{ word.word }}</h2>
            <div class="question">
                <label for="">Zenbat letrak? </label>
                <input type="text">
            </div>            
            <div class="question">
                <label for="">Zenbat silabak? </label>
                <input type="text">
            </div>

        </article>
    </section>
    <div>
        <button @click="results">BUKATUTA</button>
        <button>JOLASTU BERRIRO</button>
    </div> 

</template>

<script>


export default {
    name: "CountlettersRandom",
    data() {
        return {
            words:[], 
            word:[], 
        };
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
    padding: 5px;
}
</style>