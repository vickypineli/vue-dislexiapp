<template>
    <h1>JARDUERAK </h1>
  <section class="activity-list">
    <ActivityListItem
      v-for="activity in activities"
      :key="activity.id"
    />
  </section>
  <section>
        <router-link to="/activities/word-by-word"><button>HITZEZ HITZ</button></router-link>
        <router-link to="/activities/play-word-by-word"><button>IRAKUR-LAGUN</button></router-link>
        <router-link to="/activities/count-letters"><button>SILABAK ZENBATU</button></router-link>
        <router-link to="/activities/color-memory"><button>MARGOTU ZURE MEMORIA</button></router-link>
        <router-link to="/activities/cards-game"><button>BIKOTE JOLASA</button></router-link>
  </section>


</template>

<script>
import ActivityListItem from "./ActivityListItem.vue";
import { getActivities } from "@/services/api.js";

export default {
  name:"ActivityPage",
  components:{
    ActivityListItem,
  },
  data() {
    return {
      activities: [],
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      this.activities = await getActivities();
    },
  },


}
</script>

<style scoped>

</style>
