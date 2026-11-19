<template>
  <nav class="menu">
    <RouterLink to="/tutores">Tutores</RouterLink>
    <RouterLink to="/pets">Pets</RouterLink>
  </nav>
</template>

<style>
.menu {
  background: #42b883;
  padding: 15px;
  text-align: center;
}

.menu a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  margin: 0 15px;
}

.menu a.router-link-active {
  border-bottom: 2px solid white;
}
</style>