<script setup>
    import { RouterView, RouterLink } from 'vue-router'
    import { useDark, useToggle } from '@vueuse/core'

    import Header from './components/Header.vue'
    import Footer from './components/Footer.vue'

    const isDark = useDark({
        selector: "body",
        attribute: "theme",
        valueDark: "dark",
        valueLight: "light"
    })

    const toggleDark = useToggle(isDark)

</script>

<template>
    <div class="container">
        <Header/>
        <RouterView />
        <div class="search">
            <router-link to="/search">search</router-link>
            <svg 
                @click="toggleDark()" 
                viewBox="0 0 100 100" 
                xmlns="http://www.w3.org/2000/svg"
                :fill="isDark ? '#0B1D23' : '#B25A38'"
            >
            <circle cx="50" cy="50" r="40"/>
            </svg>
            <svg 
                @click="toggleDark()" 
                viewBox="0 0 100 100" 
                xmlns="http://www.w3.org/2000/svg"
                :fill="isDark ? '#DA9653' : '#EBE8F1'"
            >
                <circle cx="50" cy="50" r="40"/>
            </svg>
        </div>
        <Footer />
    </div>
</template>

<style>
@import './assets/reset.css';
@import './assets/font.css';
@import './assets/base.css';
@import './assets/main.css';
</style>

<style scoped>
    #app {
        height: 100%;
    }
</style>