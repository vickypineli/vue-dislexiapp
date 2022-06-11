<template>
<section class="container">
    <h1>MARGOTU ZURE MEMORIA</h1>
    <button @click="initGame">HAZI JOLASTEN</button>
    <p> aukeratu zure kolorea</p>
      <div id="app">
    <ColorSelected :color="color" />
    <ColorPicker :colors="colors" @setColor="setColor" />
  </div>
  </section>
</template>

<script>
import ColorSelected from './ColorSelected.vue';
import ColorPicker from './ColorsBox.vue';
export default {
  name:"ColorMemory",
  components: {
    ColorSelected,
    ColorPicker,
  },
  data() {
        return {
            firstime:true, 
            numofcolors: 3,
            color: "#fffff",
            colors : [
                    '#0303b7',
                    '#b7039b',
                    '#07f219',
                    '#ff6c00',
                    '#ff0000',
                    // '#ffff07',
                    // '#ff00e2',
                    // '#00e2ff',
                    // '#000000'
                     ],

        }
    },
    // mounted() {
    //     this.initGame();
    // },
    methods:{
      setColor(color){
        this.color = color;
        console.log(color)
      }
        // async initGame() {
        //   if(this.firstTime == true) {
        //       createCards();
        //       this.firstTime = false;
        //   } else {
        //       animateColorPicker();
        //       colorCards();
        //   }
      // }
    }
  

}
</script>

<style>
.color {
  display: flex;
  border: 1px solid #AAA;
  height: 30px;
  width: 30px;
  margin: 5px;
  border-radius: 25px;
}
</style>