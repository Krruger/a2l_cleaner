<script setup>
import AddPattern from './components/AddPattern.vue'
import UploadA2L from './components/UploadA2L.vue'
</script>

<template>
  <div class="container">
    <header>
      <h1>A2L Cleaner</h1>
      <p>Dodaj ciągi do usunięcia i wyślij plik A2L</p>
    </header>

    <section class="section">
      <AddPattern />
    </section>

    <section class="section">
      <UploadA2L />
    </section>
  </div>
</template>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  padding: 2rem;
  font-family: Arial, sans-serif;
}

header {
  text-align: center;
  margin-bottom: 2rem;
}

.section {
  margin-bottom: 2rem;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
}
</style>
