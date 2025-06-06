<template>
  <div>
    <input v-model="pattern" placeholder="Wpisz ciąg" />
    <button @click="add">Dodaj</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '@/api'

const pattern = ref('')

const add = async () => {
  await api.post('/pattern/', { value: pattern.value })
  pattern.value = ''
}
</script>
