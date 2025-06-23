<template>
  <div>
    <h2>Plans for Today</h2>
    <input type="date" v-model="selectedDate" @change="fetchPlans" />
    <ul>
      <li v-for="plan in plans" :key="plan.id">
        {{ plan.start_date }} to {{ plan.end_date }}: {{ plan.glasses_per_day }} glasses
        <ul>
          <li v-for="t in plan.glass_times">{{ t }}</li>
        </ul>
        <button @click="deletePlan(plan.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedDate: new Date().toISOString().substr(0, 10),
      plans: []
    };
  },
  mounted() {
    this.fetchPlans();
  },
  methods: {
    async fetchPlans() {
      const res = await axios.get(`http://localhost:5000/api/plans/${this.selectedDate}`);
      this.plans = res.data;
    },
    async deletePlan(id) {
      await axios.delete(`http://localhost:5000/api/plans/${id}`);
      this.fetchPlans();
    }
  }
};
</script>
