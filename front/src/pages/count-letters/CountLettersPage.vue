<template>
  <h1>SILABAK ZENBATU</h1>
</template>

<script>
export default {
    name:"Count-letters",
    data() {
        return {
            text:"",

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
        this.texts = await response.json();
        },
    },
};
</script>

<style>

</style>