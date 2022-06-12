<template>
    <p>Completado en  {{ turns }} turnos!</p>
    <button class="enviar" @click="$emit('click')">
    Play Again
    </button>
</template>

<script>
export default {
  name: 'Marker',
  props: ['turns'],
}
</script>

<style>

</style>