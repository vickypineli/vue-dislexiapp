<template>
  <section class="container">
      <h1>MARGOTU ZURE MEMORIA</h1>
      <button @click="initGame = !initGame" :class="styles">
          <div v-if="!initGame">HASI JOLASTEN</div>
          <div v-else>JOLASTEN BERRIRO</div>
      </button>
        <ColorBox :colors="colors" @setColor="setColorRandom" />
  </section>
  <section> 
      <div id="app">
        <ColorSelected :color="color" />
        <ColorBox :colors="colors" @setColor="setColor" />
      </div>
  </section>
</template>

<script>
import ColorSelected from './ColorSelected.vue';
import ColorBox from './ColorsBox.vue';
// import TweenLite from "gsap";


export default {
  name:"ColorMemory",
  components: {
    ColorSelected,
    ColorBox,
  },
  data() {
    return {
      firstime: true, 
      numofcolors: 3,
      color: "",
      colors : [
            '#0303b7',
            '#a30091',
            '#07f219',
            '#ff6c00',
            '#ff0000',
            '#ffff07',
            '#ff68ee',
            '#00e2ff',
            '#000000'
            ],
      CARDS_NUM:0,
      selectCard:"",
      initGame:true,
      setColorRandom:""
      }
    },
    watch:{
        initGame(value){
            if(value){
                    this.CrearCartasContainer();           
            } else {
                    return false;
            }
        }
    },
    methods:{
      setColor(color){
        this.color = color;
        console.log(color)
      },
   
      // CrearCartasContainer() {
      //   // clear data and color cards
      //   var newcolorlist = this.colors;
      //     for(var i=0; i<newcolorlist.length;i++) {
      //       //color
      //       var randomColor = this.colors[Math.floor(Math.random()*this.colors.length)];
      //       newcolorlist[i].style.background = '';
           
      //       newcolorlist[i].myColor = randomColor;
      //       setTimeout(this.hideColors, 2000, newcolorlist[i]);
      //       //clear data
      //       newcolorlist[i].innerHTML = '';
      //       newcolorlist[i].guessedFlag = false;
            
      //   }
      // }
  } 
}
</script>

<style>
.container{
  height: 30vh;
}
.color {
  display: flex;
  border: 1px solid #AAA;
  height: 30px;
  width: 30px;
  margin: 5px;
  border-radius: 25px;
}
</style>