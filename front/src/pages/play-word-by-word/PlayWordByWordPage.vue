<template>
    <h1>PLAY TEXT</h1>
        <section>
          <div id="read_List">
              <h1 id="salida"></h1>
          </div>
          <button onclick="textStart();">PLAY</button>
          <button onclick="textStop();">PAUSE</button> 
      </section>
      <!-- <section>
      <form>
          <h3> AUKERATU TESTUA: </h3>
              <input type="checkbox" id="TESTUA">1-ingles
              <input type="checkbox" id="TESTUA">2-euskera
              <input type="checkbox" id="TESTUA">3-castellano  
        
          <h3> HITZ MINUTURO: </h3>
              <input type="number" id="ppp" value="3000">
          
          <h3> TIPO DE LETRA:</h3>
              <input type="checkbox" id="fuente">Arial
              <input type="checkbox" id="fuente">Escolar
              <input type="checkbox" id="fuente">Dislexia  
      </form>
      <form>
          <button type="button" onclick="saveValues()">
              SAVE
          </button>
      </form>  
  </section> -->
</template>

<script>
export default {
    name: 'PlayText',
    data(){
      return {
      texto: "",
      palabra: 'null',
      textArray: [],
      texto1: "",


      }
    },
mounted(){
  this.loadData()
},
methods(){
  async loadData() {
    this.texto1 = {"language" : "spanish", 'text': "I can't believe the news today. Oh I can't close my eyes and make it go away"}
  }
},

}
        this.texto1 = "I can't believe the news today. Oh I can't close my eyes and make it go away";
        this.palabra = 0;
        var textArray  = this.texto1.split(" ");
       
        // saveValues = function (){
        //      fuente = document.getElementById("fuente").value;
        //      texto = document.getElementById("texto").value;
        //      ppp = document.getElementById("ppp").value;
        //      lector = document.getElementById("lector").value;
        //     console.log(fuente+""+ 
        //     texto+" "+ ppp+ " "+ lector);
        // }
        function textStart() {
            play = setInterval(textInDisplay,400);  
        }
        function textStop() {
            pause = clearInterval(textInDisplay);
        }
        function textInDisplay() {
            document.getElementById("salida").innerHTML = textArray[palabra];                             
            if(palabra >= textArray.length -1){       
                clearInterval(textInDisplay);
            }else{
                palabra++; 
            } 
    }; 
</script>

<style>
body {
      text-align: center;
    }
    section{
      margin: 1.5em;
      border: 0.3em solid red;
      padding: 1.5em;
    }
</style>

    