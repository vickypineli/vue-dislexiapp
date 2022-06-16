<template>
    <p>Activity item</p>
    <article class="activity-item">
        <p>{{ activity.name }}</p>
        <router-link :to="`/activities/${activity.route}`"><button>-klik!-</button></router-link>
    </article>
</template>

<script>
export default {
  props: {
    activity: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.activity-item {
  border: 1px solid rgb(119, 115, 115);
  border-radius: 1em;
  margin: 1em;
}
</style>
