<template>
    <h1>HITZEZ HITZ</h1>

<form>
   <p>
    <label>Letra-tipo</label>
    <select
      id="font"
      v-model="fontseleted"
    >
      <option>Arial</option>
      <option>Escolar</option>
      <option>Dislexia</option>
    </select>
  </p> 
  <p>
    <label>Hitz-minuturo</label>
    <input
      id="wordByWord"
      v-model="wordByWord"
      type="number"
      min="30"
      max="100">
  </p>

  <p>
    <label>Aukeratu testua</label>
    <select
      
      id="textselected"
      v-model="textselected"
      name="textselected"
    >
      <option>Testu 1</option>
      <option>Testu 2</option>
      <option>Testu 3</option>
    </select>
  </p>
  <p>
    <label>Entzun</label>
    <select
      
      id="voiceselected"
      v-model="voiceselected"
    >
      <option>Bai</option>
      <option>Ez</option>
    </select>
  </p>

  <p>
    <input
      type="submit"
      value="Datuak gorde"
    >
  </p>

</form>
</template>

<script>
export default {

}
</script>

<style>

</style>