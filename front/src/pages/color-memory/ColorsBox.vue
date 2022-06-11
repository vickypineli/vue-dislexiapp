<template>
  <div class="colorbox">
    <div 
      class="color"
      v-for="(color, i) in colors"
      :key="i"
      :style="'background:'+color"
      @click="setColor(color)"></div>
  </div>
</template>

<script>
export default {
  name: 'color-box',
  props: {
      colors:{type:String}
      },
  methods: {
    setColor (color) {
      this.$emit('setColor', color);
    }
  }
}
</script>

<style scoped>
.color-picker {
  width: 90vw;
  margin: auto;

}
.color {
  border: 1px solid #AAA;
  width: 40px;
  height: 40px;
 

}
</style>
