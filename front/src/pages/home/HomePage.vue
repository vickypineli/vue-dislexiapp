<template>
  <h1>IRLA-KURRI</h1>
  <section id="home-container">
      <article class="logo-box">
        <img src="@/assets/img/irlakurri.png" alt="logo">
      </article>
      <article class="login-box">
        <div class="login-date">
          <label>Izena:</label>
          <input  type="text" v-model="user" />
        </div>
        <div class="login-date">
          <label>Pasahitza:</label>
          <input class="input-internal" type="password" v-model="password" />
        </div>
        <div class="login-date">
          <button @click="onButtonClicked">SARTU</button>
        </div>
        
      </article>
      
  </section>

</template>

<script>
import { useStorage } from "@vueuse/core";
import { login } from "@/services/auth.js";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Home',
  data() {
    return {
      user: "",
      password: "",
      localUser: useStorage("auth", {}),

    }
  },

  methods: {

   async onButtonClicked() {

      const response = await login(this.user, this.password);
      
      const loginStatus = response.status;
      const loginUser = await response.json();
 

      if (loginStatus === 401) {
        alert("unauthorized");
      } else {
        this.localUser = loginUser.name;
        this.$router.push("/activities");
      }
    },
  }

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Slackey&display=swap');

#home-container{
  width: 90vw;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin: auto;
}

.logo-box {
  width: 40vw;
  display: flex;
  justify-content: center;
  margin: auto;
}

.login-box {
  width: 40vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: 25px;
  border: 2px dashed rgb(255, 0, 85);
  border-radius: 5px;
 
}
.login-date{
  margin: 10px;
  display: flex;
  flex-direction: column;

}

h1 {
  width: 90vw;
  height: 10vh;
  margin: auto;
  font-family: 'Slackey';
  font-size: 4vw;
  text-transform: uppercase;
  color: rgb(242, 117, 8);
}
img {
  width: 35vw;
  height: 30vw;
}
label{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  text-align: left;
  font-weight: bold;
  color: #217a52;
  font-size: 1.5em;
}
input {
  height: 4.5vh;
  font-size: 1.5em;
}

button {
  width: 30vw;
  height: 5vh;
  margin: auto;
  padding: 5px 10px;
  font-size: 1em;
  border-color:gray;
  border-radius: 15px;
  background: #42b983;
  color:white;
}
</style>
