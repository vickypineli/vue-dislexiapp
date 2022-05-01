<template>
  <section class="home">
      <div>
        <h1>IRLA-KURRI</h1>
        <img src="@/assets/img/irlakurri.png" alt="logo">
      </div>
      <div class="users">
        <select v-model ="selectedUser">
          <option :value="null">Erabiltzaile izena</option>
          <option v-for="user in users" :value="user" :key="user.id">
            {{ user.name }}
          </option>
        </select>
        <button @click="onButtonClicked">SARTU</button>
      </div>
  </section>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      info: {},
      users:[],
      selectedUser:null,
    }
  },
  mounted() {
    this.loadData()
    this.loadUsers()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/activities')
      this.info = await response.json()
  
  },
  async loadUsers() {
      this.users = [
        {
          id: "user-1",
          name: "pepa",
        },
        {
          id: "user-2",
          name: "pepe",
        },
      ];
    },

   onButtonClicked() {
      localStorage.userId = this.selectedUser.id;
      localStorage.userName = this.selectedUser.name;
      this.$router.push("/activities");
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
