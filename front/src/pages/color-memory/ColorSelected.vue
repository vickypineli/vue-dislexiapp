<template>
  <div id="colorselected">
    <h3>kolorea:</h3>
    <div class="color" :style="'background:'+color"></div>
  </div>
</template>

<script>
export default {
  name: 'ColorSelected',
  props: ['color']
}
</script>

<style scoped>
#colorselected{
  width: 50vw;
  height: 15vh;
  margin: auto;
  display: flex;
  justify-content: center;
}
.color {
  width: 80px;
  height: 40px;
  
  border: 1px dashed #F3F3F3;
  border-radius: 0%;
}
</style>
