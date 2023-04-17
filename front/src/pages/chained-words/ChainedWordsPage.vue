<template>
    <h1>HITZ KATEATUAK</h1>
  <section class="container">
    <h2>AUKERATU MAILA</h2>
    <div class="buttons-area">
    <router-link to="/activities/chained-words/easy"><button>ERRASA</button></router-link>
    <router-link to="/activities/chained-words/mediun"><button>NORMALA</button></router-link>
    <router-link to="/activities/chained-words/hard"><button>ZAILENA</button></router-link>
  </div>
</section>
</template>
<script>
export default {
  name:"ChainedWord",
  data() {
        return {
        }
  },
} 
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Slackey&display=swap");
.container {
    margin:auto;
    width: 90vw;
    margin: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border: 4px dashed #42b983;
    border-radius: 10px;
    
}
.buttons-area{
    width: 90vw;
    height: 30vh;
    margin: auto;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-around;
}
.text{
    font-size: 1.5em;
    padding: 15px;
}
h1 {
  width: 90vw;
  height: 90px;
  margin: auto;
  margin-top: 5vh;
  font-size:5vw ;
  font-family: 'Slackey';
  text-transform: uppercase;
  color: rgb(242, 117, 8);
}
h2{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  color:rgb(247, 9, 88);  
}
button {
    width:300px;
    height: 8vh;
    margin: auto;
    padding: 5px 10px;
    border-color:rgb(145, 144, 144);
    border-radius: 10px;
    font-family: dislexia;
    font-size: 1.5em;
    background: #42b983;
    color: white;
}
</style>