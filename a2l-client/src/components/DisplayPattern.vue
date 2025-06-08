<template>
  <div>
    <h2>Lista ciągów:</h2>
    <ul>
      <li v-for="item in strings" :key="item.id">
        {{ item.value }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api'

const strings = ref([])

onMounted(async () => {
  const res = await api.get(`/strings/`)
  console.log(res)
  strings.value = res.data
})
</script>
