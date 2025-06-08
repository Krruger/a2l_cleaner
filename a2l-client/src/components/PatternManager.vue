<template>
  <div class="max-w-xl mx-auto space-y-6 p-6">
    <h2 class="text-3xl font-semibold text-gray-800">Zestawy Patternów</h2>

    <!-- Tworzenie nowej grupy -->
    <div class="flex gap-2">
      <input v-model="newGroupName" class="input" placeholder="Nazwa nowej grupy" />
      <button @click="createNewGroup" class="btn-primary">Dodaj grupę</button>
    </div>

    <!-- Wybór istniejącej grupy -->
    <div>
      <label class="block text-sm font-medium mb-1">Wybierz grupę:</label>
      <select v-model="selectedGroupId" class="input w-full">
        <option disabled value="">-- wybierz --</option>
        <option v-for="group in groups" :key="group.id" :value="group.id">{{ group.name }}</option>
      </select>
    </div>

    <!-- Dodawanie patternów -->
    <div v-if="selectedGroupId" class="flex gap-2">
      <input v-model="newPattern" class="input w-full" placeholder="Nowy pattern" />
      <button @click="addPattern" class="btn-secondary">Dodaj</button>
    </div>

    <!-- Lista patternów -->
    <div v-if="patterns.length" class="bg-white shadow rounded-lg p-4">
      <h3 class="font-semibold mb-2">Zdefiniowane patterny:</h3>
      <ul class="list-disc list-inside space-y-1">
        <li v-for="p in patterns" :key="p.id">{{ p.value }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { getGroups, createGroup, getPatterns, addPatternToGroup } from '../api'

const newGroupName = ref('')
const groups = ref([])
const selectedGroupId = ref('')
const patterns = ref([])
const newPattern = ref('')

async function loadGroups() {
  groups.value = await getGroups()
}

async function createNewGroup() {
  if (!newGroupName.value) return
  await createGroup(newGroupName.value)
  newGroupName.value = ''
  await loadGroups()
}

async function addPattern() {
  if (!newPattern.value || !selectedGroupId.value) return
  await addPatternToGroup(newPattern.value, selectedGroupId.value)
  newPattern.value = ''
  await loadPatterns()
}

async function loadPatterns() {
  if (selectedGroupId.value) {
    patterns.value = await getPatterns(selectedGroupId.value)
  }
}

watch(selectedGroupId, loadPatterns)

onMounted(loadGroups)
</script>

<style scoped>
@import "tailwindcss";
.input {
  @apply border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500;
}

.btn-primary {
  @apply bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition;
}

.btn-secondary {
  @apply bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition;
}
</style>
