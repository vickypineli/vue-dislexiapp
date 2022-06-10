<template>
  <section class="home">
      <div>
        <h1>IRLA-KURRI</h1>
        <img src="@/assets/img/irlakurri.png" alt="logo">
      </div>
      <div>
          <label>Usuario:</label>
          <input type="text" v-model="user" />
          <label>Clave:</label>
          <input type="password" v-model="password" />
      </div>
      <button @click="onButtonClicked">SARTU</button>
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
      user: "",
      password: "",
      localUser: useStorage("user", {}),

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
h1 {
  font-style: italic;
  font-family: 'Slackey';
  font-size: 2.5em;
  text-transform: uppercase;
  color: rgb(242, 117, 8);

}
button {
  margin: 10px;
  padding: 5px 10px;
  border-color:gray;
  border-radius: 25px;
  font-size: 1em;
  background: #42b983;
  color:white;
}
</style>
