<script setup>

    import { ref } from 'vue'

    import { RouterLink } from 'vue-router'

    import Glyph from '../components/utils/Glyph.vue'
    import Cross from '../components/utils/Cross.vue'

    let active = ref(false)

    function handleClick(e) {
        console.log(e)
        active.value = !active.value
    }

</script>

<template>

    <header>
        
        <div class="titre">
            <RouterLink to="/">Our <span>Collaborative</span> Tools</RouterLink>
        </div>
        
        <div class="titre_mobile">
            <RouterLink to="/">O<span>C</span>T</RouterLink>
        </div>

        <nav class="navigation">
            <RouterLink to="/">Index</RouterLink>
            <RouterLink to="/articles">Articles</RouterLink>
            <RouterLink to="/notions">Notions</RouterLink>
            <RouterLink to="/authors">Authors</RouterLink>
            <RouterLink to="/mediagraphy">Media</RouterLink>
            <RouterLink to="/search">Search</RouterLink>
            <RouterLink to="/about">about</RouterLink>
        </nav>

        <glyph
            class="navigation_mobile_glyph" 
            width="50" 
            height="50"
            @click="handleClick"    
        ></glyph>

        <nav 
            class="navigation_mobile"
            :style="{
                display: active ? 'block' : 'none'
            }"
        >
            <cross 
                width="60" 
                height="60"
                @click="handleClick" 
            ></cross>
            <div class="navigation--menu">
                <RouterLink @click="handleClick" to="/">Index</RouterLink>
                <RouterLink @click="handleClick" to="/articles">Articles</RouterLink>
                <RouterLink @click="handleClick" to="/notions">Notions</RouterLink>
                <RouterLink @click="handleClick" to="/authors">Authors</RouterLink>
                <RouterLink @click="handleClick" to="/mediagraphy">Media</RouterLink>
                <RouterLink @click="handleClick" to="/about">about</RouterLink>
                <RouterLink @click="handleClick" to="/search">search</RouterLink>
            </div>
        </nav>
      
    </header>

</template>

<style scoped>

    .navigation > .router-link-exact-active {
        text-decoration: underline;
    }

    .navigation--menu > .router-link-exact-active {
        text-decoration: underline;
    }

</style>