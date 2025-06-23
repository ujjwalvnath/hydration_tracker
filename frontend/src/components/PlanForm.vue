<template>
  <div>
    <h2>Create Hydration Plan</h2>
    <form @submit.prevent="createPlan">
      <label>Start Date: <input type="date" v-model="startDate" /></label><br>
      <label>End Date: <input type="date" v-model="endDate" /></label><br>
      <label>Glasses/Day: <input type="number" v-model.number="glassesPerDay" /></label><br>
      <div v-for="(time, index) in glassTimes" :key="index">
        <input type="time" v-model="glassTimes[index]" />
      </div>
      <button type="button" @click="addGlassTime">Add Glass Time</button><br>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      startDate: '',
      endDate: '',
      glassesPerDay: 0,
      glassTimes: []
    };
  },
  methods: {
    addGlassTime() {
      this.glassTimes.push('');
    },
    async createPlan() {
      await axios.post('http://localhost:5000/api/plans', {
        user_id: 1,
        start_date: this.startDate,
        end_date: this.endDate,
        glasses_per_day: this.glassesPerDay,
        glass_times: this.glassTimes
      });
      this.$emit('refresh');
    }
  }
};
</script>
