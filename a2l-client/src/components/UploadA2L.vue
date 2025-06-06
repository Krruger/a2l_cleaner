<template>
  <div>
    <input type="file" @change="handleFile" />
    <button @click="upload">Wyślij</button>
    <div v-if="response">{{ response }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '@/api'

const file = ref(null)
const response = ref(null)

const handleFile = (e) => {
  file.value = e.target.files[0]
}

const upload = async () => {
  const formData = new FormData()
  formData.append('file', file.value)
  const res = await api.post('/upload/', formData)
  response.value = 'Zapisano jako: ' + res.data.filename
}
</script>
