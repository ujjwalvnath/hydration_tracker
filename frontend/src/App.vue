<template>
  <div id="app">
    <h1>Water Hydration Scheduler</h1>
    <PlanForm />
    <PlanList />
  </div>
</template>

<script>
import PlanForm from './components/PlanForm.vue';
import PlanList from './components/PlanList.vue';

export default {
  name: 'App',
  components: {
    PlanForm,
    PlanList
  }
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  padding: 20px;
}
</style>
