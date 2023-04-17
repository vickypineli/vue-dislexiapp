
<template>
    <p>JOKO MARKAGAILU</p>
    <p> -{{ turns }}-TXANDATAN BAT!</p>
    <button class="enviar" @click="$emit('click')">
    Play Again
    </button>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Marker',
  props: ['turns'],
}
</script>

<style>

</style>