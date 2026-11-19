<script setup>
import { ref, onMounted } from 'vue'

const url = 'http://127.0.0.1:8000'

const pets = ref([])
const petSelecionado = ref(null)

// Busca a lista quando a página abre
onMounted(async () => {
  const resposta = await fetch(url + '/listarpets')
  pets.value = await resposta.json()
})

// Consulta um pet pelo id
async function consultarPet(id) {
  const resposta = await fetch(url + '/consultarpet/' + id)
  petSelecionado.value = await resposta.json()
}
</script>

<template>
  <div class="pagina">
    <h1>Pets</h1>

    <ul>
      <li v-for="pet in pets" :key="pet.id">
        {{ pet.nome }}
        <button @click="consultarPet(pet.id)">Consultar</button>
      </li>
    </ul>

    <div v-if="petSelecionado" class="detalhe">
      <p>ID: {{ petSelecionado.id }}</p>
      <p>Nome: {{ petSelecionado.nome }}</p>
      <p>Espécie: {{ petSelecionado.especie }}</p>
      <p>ID do tutor: {{ petSelecionado.tutor_id }}</p>
    </div>
  </div>
</template>