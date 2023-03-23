<script setup>

    import { RouterLink } from 'vue-router'

    // import { storeToRefs } from 'pinia'

    // import { useThemeStore } from '../store/theme'

    // const { setTheme, isDark } = useThemeStore()

  

</script>

<template>

    <header>
        <RouterLink class="titre" to="/">Our <span>Collaborative</span> Tools</RouterLink>
        <nav>
            <RouterLink to="/">Index</RouterLink>
            <!-- <RouterLink to="/articles">Articles</RouterLink> -->
            <RouterLink to="/notions">Notions</RouterLink>
            <RouterLink to="/authors">Authors</RouterLink>
            <!-- <RouterLink to="/licences">Licences</RouterLink> -->
            <!-- <RouterLink to="/search">Search</RouterLink> -->
            <RouterLink to="/about">about</RouterLink>
            
        </nav>
      
    </header>

</template>

<style scoped>

    .router-link-exact-active {
        text-decoration: underline;
    }

</style>