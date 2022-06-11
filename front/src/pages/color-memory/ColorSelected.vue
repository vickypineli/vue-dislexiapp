<template>
  <div id="colorselected">
    <h3>Aukeratutako kolorea:</h3>
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
  width: 80vw;
  height: 10vh;
  margin: auto;
  display: flex;
  justify-content: center;
}
.color {
  width: 80px;
  height: 45px;
  border: 1px dashed #F3F3F3;
  border-radius: 15%;
}
</style>
