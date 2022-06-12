<template>
  <h1>BIKOTE AURKITZEN</h1>
  <Cards
        v-for="mask in masks"
        :key="mask.id"
        :card="mask"
        @click="handleClick"
        :active="
        firstPick === mask || secondPick === mask || mask.matched
        "
  />
  <div>Turns: {{ turns }}</div>
  <Marker v-show="done" :turns="turns" @click="resetGame"/>
</template>

<script>
import Cards from "./Cards.vue";
import Marker from "./Marker.vue";
export default {
    name:"Game",
    components:{
        Cards,
        Marker,
    },
    data(){
        return{
            masks: [],
            firstPick: null,
            secondPick: null,
            turns: 0,
            done: false,
            images:[
                { img: "masc1.png" },
                { img: "masc2.png" },
                { img: "masc3.png" },
                { img: "masc4.png" },
                { img: "masc5.png" },
                { img: "masc6.png" },
            ]
        }
    }


}
</script>

<style>

</style>