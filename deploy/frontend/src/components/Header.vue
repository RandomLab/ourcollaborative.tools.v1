<script setup>

    import { RouterLink } from 'vue-router'

</script>

<template>

    <header>
        <RouterLink class="titre" to="/">Our <span>Collaborative</span> Tools</RouterLink>
        <nav>
            <RouterLink to="/">Index</RouterLink>
            <RouterLink to="/notions">Notions</RouterLink>
            <RouterLink to="/authors">Authors</RouterLink>
            <RouterLink to="/about">about</RouterLink>
            
        </nav>
      
    </header>

</template>

<style scoped>

    .router-link-exact-active {
        text-decoration: underline;
    }

</style>