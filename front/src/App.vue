<template>
  <div id="nav">
    <router-link to="/">Hasiera</router-link>|
    <router-link to="/activities">Jarduerak</router-link>|
    <p>{{ }} </p>
  </div>
  <router-view />
</template>
<script>
import { useStorage } from "@vueuse/core";

export default {
  data() {
    return {
      localUser: useStorage("user", {}),
    };
  },
  computed: {
    loggedUser() {
      return this.localUser.name;
    },
  },
};
</script>
