// // src/api.js
// import axios from 'axios'

// const instance = axios.create({
//   baseURL: import.meta.env.VITE_API_URL,
// })

// export default instance

import axios from 'axios'

const api = import.meta.env.VITE_API_URL

export async function getGroups() {
  const res = await axios.get(`${api}/groups/`)
  return res.data
}

export async function createGroup(name) {
  console.log(`${api}/groups/`)
  const res = await axios.post(`${api}/groups/`, { name })
  return res.data
}

export async function getPatterns(groupId) {
  const res = await axios.get(`${api}/patterns/${groupId}`)
  return res.data
}

export async function addPatternToGroup(value, groupId) {
  const res = await axios.post(`${api}/patterns/`, { value, group_id: groupId })
  return res.data
}
