<template>
  <div>
    <h2>{{ editingWineId ? "Edit Wine" : "Add Wine" }}</h2>

    <input v-model="form.name" placeholder="Name" />
    <input v-model="form.country" placeholder="Country" />
    <input v-model="form.type" placeholder="Type" />
    <input v-model.number="form.price" type="number" placeholder="Price" />
    <input v-model="form.description" placeholder="Description" />

    <button @click="addWine">
      {{ editingWineId ? "Save Changes" : "Add Wine" }}
    </button>

    <hr />

    <div v-for="wine in wines" :key="wine.id">
      {{ wine.name }} - {{ wine.country }} - {{ wine.price }}

      <button @click="editWine(wine)">Edit</button>
      <button @click="deleteWine(wine.id)">Delete</button>
    </div>

    <hr />

    <!-- Pagination -->
    <button :disabled="page === 1" @click="prevPage">Prev</button>
    <span>Page {{ page }}</span>
    <button :disabled="page * limit >= total" @click="nextPage">Next</button>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  name: "WinesView",

  data() {
    return {
      wines: [],
      editingWineId: null,   // 👈 ТУКА
      page: 1,
      limit: 5,
      total: 0,
      form: {
        name: "",
        country: "",
        type: "",
        price: null,
        description: "",
      },
    };
  },

  mounted() {
    this.loadWines();
  },

  methods: {
    async loadWines() {
      const res = await api.get("/wines", {
        params: { page: this.page, limit: this.limit },
      });
      this.wines = res.data.data;
      this.total = res.data.total;
    },

    editWine(wine) {
      this.editingWineId = wine.id;
      this.form = { ...wine };
    },

    async addWine() {
      if (this.editingWineId) {
        // UPDATE
        await api.put(`/wines/${this.editingWineId}`, this.form);
        this.editingWineId = null;
      } else {
        // ADD
        await api.post("/wines", this.form);
      }

      await this.loadWines(); // 👈 Variant A: refresh after save
      this.resetForm();
    },

    async deleteWine(id) {
      await api.delete(`/wines/${id}`);
      await this.loadWines();
    },

    prevPage() {
      if (this.page > 1) {
        this.page--;
        this.loadWines();
      }
    },

    nextPage() {
      if (this.page * this.limit < this.total) {
        this.page++;
        this.loadWines();
      }
    },

    resetForm() {
      this.form = {
        name: "",
        country: "",
        type: "",
        price: null,
        description: "",
      };
    },
  },
};
</script>
