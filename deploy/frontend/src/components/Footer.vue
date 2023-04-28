<script setup>

    import { RouterLink } from 'vue-router'

</script>

<template>
    <footer>
        <RouterLink to="/">Projects</RouterLink>
        <RouterLink to="/articles">Articles</RouterLink>
        <RouterLink to="/notions">Notions</RouterLink>
        <RouterLink to="/authors">Authors</RouterLink>
        <RouterLink to="/mediagraphy">Media</RouterLink>
        <RouterLink to="/search">search</RouterLink>
        <RouterLink to="/about">about</RouterLink>
    </footer>
</template>