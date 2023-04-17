<template>
  <p>CARTA</p>
  <div
    :class="{'flipped' : active}"
    @click="handleClick">
  </div>
  <div class="front">
      <img class="up" src="require(`/assets/img/${card.img}`)" alt="faceUp">
      <img class="back" src="/assets/img/irlakurri.png" alt="faceDown">
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name:"Card",
  props: ['card','active'],
  methods : {
    handleClick(){
      if(!this.active){
        this.$emit('click', this.card);
      }
    }
  }
}
</script>

<style>
.front {
  transform: rotateY(90deg);
  transition: all ease-in 0.2s;
  position: absolute;
}
.flipped .front {
  transform: rotateY(0deg);
  transition-delay: 0.2s;
}
.back {
  transition: all ease-in 0.2s;
  transition-delay: 0.2s;
}
.flipped .back {
  transform: rotateY(90deg);
  transition-delay: 0s;
}
</style>