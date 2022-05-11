<template>
  <h1>SILABAK ZENBATU</h1>
    <article
        class="contact-item"
        v-for="word in words"
        :key="word.id"
    >
        <img class="photo" :src="word.img" />
        <h2>{{ word.word }}</h2>

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

<style>
.photo {
    width: 200px;  
}
p {
    font-size: 30px;
}
</style>