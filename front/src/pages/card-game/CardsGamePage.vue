<template>
  <h1>BIKOTE AURKITZEN</h1>
  <Cards/>
  <Marker/>
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

}
</script>

<style>

</style>