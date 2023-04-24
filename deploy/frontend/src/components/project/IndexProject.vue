<script setup>

    import { ref } from 'vue'
    import { useRouter, useRoute } from 'vue-router'
   
    import Icon from '../../components/utils/Glyph.vue'
    
    const router = useRouter()

    const props = defineProps(['project'])

    const hover = ref(false)

    function gotoProject(path) {
        router.push(path)
    }

</script>

<template>
    
    <div
        class="item-detail"
        @mouseenter="hover = true"
        @mouseleave="hover = false"
        @click="gotoProject(`/project/${project.slug}`)"
    >

        <img
            :src="project.thumbnail"
            :class="hover ? 'hide' : 'show'"
        />

        <div 
            class="item-info"
            :class="hover ? 'show' : 'hide'"
        >
            <Icon width="10" height="10" />
            <h2>Author(s)</h2>
            <h3 
                v-for="author in project.author"
                :key="author.id"
            >
                {{ author.group ? null : author.firstname }} {{ author.name }}
            </h3>
            <h1>{{ project.title }}</h1>
            <p class="description">{{ project.description }}</p>
        </div>

    </div>

</template>


<style scoped>
    .show {
        display: block;
    }

    .hide {
        display: none;
    }

</style>