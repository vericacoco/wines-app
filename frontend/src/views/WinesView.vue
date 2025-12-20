<template>
  <div class="container">
    <h1 class="title">🍷 Wine Catalog</h1>

    <div class="wine-grid">
      <div class="wine-card" v-for="wine in wines" :key="wine.name">
        <h2>{{ wine.name }}</h2>
        <p class="meta">{{ wine.country }} · {{ wine.type }}</p>
        <p class="price">€{{ wine.price }}</p>
        <p class="description" v-if="wine.description">
          {{ wine.description }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  name: "WinesView",
  data() {
    return {
      wines: [],
    };
  },
  async mounted() {
    const response = await api.get("/wines");
    this.wines = response.data;
  },
};
</script>

<style scoped>
.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 2rem;
  font-family: Arial, Helvetica, sans-serif;
}

.title {
  text-align: center;
  margin-bottom: 2rem;
  color: #5a1a1a;
}

.wine-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

.wine-card {
  background: #ffffff;
  border-radius: 10px;
  padding: 1.2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.wine-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.12);
}

.wine-card h2 {
  margin: 0;
  color: #7b1e1e;
}

.meta {
  font-size: 0.9rem;
  color: #777;
  margin: 0.3rem 0;
}

.price {
  font-weight: bold;
  margin: 0.5rem 0;
  color: #2e7d32;
}

.description {
  font-size: 0.9rem;
  color: #444;
}
</style>
