<template>
  <div id="nav">
    <router-link to="/">Hasiera</router-link>
    <router-link to="/activities">Jarduerak</router-link>
    <p> KAIXO:  {{loggedUser}} </p>
  </div>
  <router-view />
</template>
<script>
import { useStorage } from "@vueuse/core";
export default {
  data() {
    return {
      localUser: useStorage("auth", {}),
    };
  },
  computed: {
    loggedUser() {
     let user = localStorage.getItem("auth");
     return user;
    },
  },
};
</script>
<style scoped>
#nav{
  height: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: baseline;
  font-family: dislexia;
}
p{
  margin-left: 100px;
  padding: 4px;
  color: rgb(255, 0, 85);
  font-weight: bold;
  border: 1px solid rgb(177, 175, 175);
  border-radius: 5px;
}
</style>
