<template>
  <h1>IRLA-KURRI</h1>
  <section id="home-container">
      <article class="logo-box">
        <img src="@/assets/img/irlakurri.png" alt="logo">
      </article>
      <article class="login-box">
        <div class="login-date">
          <label>Usuario:</label>
          <input  type="text" v-model="user" />
        </div>
        <div class="login-date">
          <label>Clave:</label>
          <input class="input-internal" type="password" v-model="password" />
        </div>
        <div class="login-date">
          <button @click="onButtonClicked">SARTU</button>
        </div>
      </article>
      
  </section>
      <!-- <div class="users">
        <select v-model ="selectedUser">
          <option :value="null">Erabiltzaile izena</option>
          <option v-for="user in users" :value="user" :key="user.id">
            {{ user.name }}
          </option>
        </select>
       </div> --> 
</template>

<script>
import { useStorage } from "@vueuse/core";
import { login } from "@/services/auth.js";

export default {
  name: 'Home',
  data() {
    return {
      // info: {},
      // users:[],
      // selectedUser:null,
      user: [],
      password: "",
      localUser: useStorage("auth", {}),

    }
  },
  // mounted() {
  //   this.loadData(),
  //   this.loadUsers()
  // },
  methods: {
  //   async loadData() {
  //     const response = await fetch('http://localhost:5000/api/activities')
  //     this.info = await response.json()
  // },
  //   async loadUsers() {
  //     const response = await fetch('http://localhost:5000/api/users')
  //       this.users = await response.json()

  //     // this.users = [
  //     //   {
  //     //     id: "user-1",
  //     //     name: "pepa",
  //     //   },
  //     //   {
  //     //     id: "user-2",
  //     //     name: "pepe",
  //     //   },
  //     // ];
  //   },

   async onButtonClicked() {
      // localStorage.userId = this.selectedUser.id;
      // localStorage.userName = this.selectedUser.name;
      // this.$router.push("/activities");
      const response = await login(this.user, this.password);
      const loginStatus = response.status;
      const loginUser = await response.json();
      console.log("response", response);
      console.log("loginUser", loginUser);

      if (loginStatus === 401) {
        alert("unauthorized");
      } else {
        this.localUser = loginUser;
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
  justify-content: center;
  flex-wrap: wrap;
  align-content: space-around;
  margin-top: 2em;
}

.logo-box {
  width: 40vw;
  display: flex;
  justify-content: center;
  margin: 25px;
}

.login-box {
  width: 40vw;
  display: flex;
  flex-direction: column;
  justify-content: center;

  margin: 25px;
 
}
.login-date{
  margin: 10px;
  display: flex;
  flex-direction: column;

}

h1 {
  width: 90vw;
  margin: auto;
  font-style: italic;
  font-family: 'Slackey';
  font-size: 2.5em;
  text-transform: uppercase;
  color: rgb(242, 117, 8);
}

img {
  width: 40vw;
  height: 30vw;
}
label{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  text-align: left;
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
  border-color:gray;
  border-radius: 25px;
  font-size: 1em;
  background: #42b983;
  color:white;
}
</style>
