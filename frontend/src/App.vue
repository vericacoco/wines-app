<template>
  <div>
    <h1>🍷 Wines App - Form </h1>
    <WinesView />
  </div>
</template>

<script>
import WinesView from "./views/WinesView.vue";

export default {
  name: "App",
  components: {
    WinesView,
  },
};
</script>
