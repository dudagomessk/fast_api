<script setup>
import { ref, onMounted } from 'vue'

const url = 'http://127.0.0.1:8000'

const tutores = ref([])
const tutorSelecionado = ref(null)

// Busca a lista quando a página abre
onMounted(async () => {
  const resposta = await fetch(url + '/tutores')
  const json = await resposta.json()
  tutores.value = json.dados
})

// Consulta um tutor pelo id
async function consultarTutor(id) {
  const resposta = await fetch(url + '/tutores/' + id)
  const json = await resposta.json()
  tutorSelecionado.value = json.dados
}
</script>

<template>
  <div class="pagina">
    <h1>Tutores</h1>

    <ul>
      <li v-for="tutor in tutores" :key="tutor.id">
        {{ tutor.nome }}
        <button @click="consultarTutor(tutor.id)">Consultar</button>
      </li>
    </ul>

    <div v-if="tutorSelecionado" class="detalhe">
      <p>ID: {{ tutorSelecionado.id }}</p>
      <p>Nome: {{ tutorSelecionado.nome }}</p>
      <p>Telefone: {{ tutorSelecionado.telefone }}</p>
    </div>
  </div>
</template>