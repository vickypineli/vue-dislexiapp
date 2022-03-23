<template>
  <h1>play</h1>
  <section class="counter">
      <h2>{{ readlist }}</h2>
      <section class="buttons">
        <button @click="playClicked">PLAY</button>
        <button @click="stopClicked">STOP</button>
      </section>
  </section>

</template>

<script>

export default {
  name: "PlayWordbyWord",
}
</script>

<style>

</style>