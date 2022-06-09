<template>
<section class="container">
  <h1>MARGOTU ZURE MEMORIA</h1>
  <button @click="initGame">HAZI JOLASTEN</button>
  <p> aukeratu zure kolorea</p>

<label class="orange">
  <input type="radio" name="color" value="orange">
  <div class="layer"></div>
  <div class="button"><span></span></div>
</label>

<label class="amber">
  <input type="radio" name="color" value="amber">
  <div class="layer"></div>
  <div class="button"><span></span></div>
</label>

<label class="lime">
  <input type="radio" name="color" value="lime">
  <div class="layer"></div>
  <div class="button"><span></span></div>
</label>

<label class="rose">
  <input type="radio" name="color" value="rose">
  <div class="layer"></div>
  <div class="button"><span></span></div>
</label>

<label class="blue">
  <input type="radio" name="color" value="blue">
  <div class="layer"></div>
  <div class="button"><span></span></div>
</label>

<label class="indigo">
  <input type="radio" name="color" value="indigo">
  <div class="layer"></div>
  <div class="button"><span></span></div>
</label>
<label class="black">
  <input type="radio" name="color" value="black">
  <div class="layer"></div>
  <div class="button"><span></span></div>
</label>
<label class="red">
  <input type="radio" name="color" value="red">
  <div class="layer"></div>
  <div class="button"><span></span></div>
</label>
<label class="white">
  <input type="radio" name="color" value="white">
  <div class="layer"></div>
  <div class="button"><span></span></div>
</label>
</section>     

</template>

<script>

export default {
  name:"ColorMemory",
  data() {
        return {
            firstime:true, 
            numofcolors: 3,
            colors : [
                    '#0303b7',
                    '#b7039b',
                    '#07f219',
                    '#ff6c00',
                    '#ff0000',
                    '#ffff07',
                    '#ff00e2',
                    '#00e2ff',
                    '#000000' ],

        }
    },
    mounted() {
        this.initGame();
    },
    methods:{
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
.container{
  border: 5px dashed red;
}
body {
  width: 100%;
  height: 100%;  
  margin: 0;
  padding: 0;
  text-align: center;
}

body {
  box-sizing: border-box;
  padding-top: 180px;
  background: #ffffff;
}

input {
  display: none;
}

.button {
  display: inline-block;
  position: relative;
  width: 50px;
  height: 50px;
  margin: 5px;
  cursor: pointer;
}

.button span {
  display: block;
  position: absolute;
  width: 50px;
  height: 50px;
  padding: 0;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  -o-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  border-radius: 100%;
  background: #eeeeee;
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.26);
  transition: ease .3s;
}

.button span:hover {
  padding: 10px;
}

.orange .button span {
  background: #fa9a33;
}

.amber .button span {
  background: #f8e003;
}

.lime .button span {
  background: #26ee14;
}

.rose .button span {
  background: #f602e2;
}

.blue .button span {
  background: #06fdf9fb;
}

.indigo .button span {
  background: #3F51B5;
}
.black .button span {
  background: #000;
}
.red .button span {
  background: rgb(244, 4, 4);
}

.layer {
  display: block;
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background: transparent;
  /* transition: ease .3s; */
  z-index: -1;
}













</style>