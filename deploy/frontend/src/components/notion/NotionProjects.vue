<script setup>

    import { ref, reactive, computed, onMounted, watchEffect } from 'vue'

    import { marked } from 'marked'

    import { useRoute } from 'vue-router'

    import { storeToRefs } from 'pinia'
    import { useNotionStore } from '../../store/notions'

    import NotionListProjects from './NotionListProjects.vue'

    const route = useRoute()

    const { notion, loading, error } = storeToRefs(useNotionStore())

    const { fetchNotionBySlug } = useNotionStore()

    onMounted(() => {
        fetchNotionBySlug(route.params.slug)
    })

    watchEffect(() => {
        fetchNotionBySlug(route.params.slug)
    })


</script>

<template>  

    <p v-if="loading">Loading post...</p>
        
    <p v-if="error">{{ error.message }}</p>
    
    <div 
        v-if="notion"
        class="notion--detail"
    >

        <h1>{{ notion.title }}</h1>
        <p v-html="marked.parse(notion.content)"></p>

        <div class="ref">projets</div>

        <notion-list-projects :id="notion.id"></notion-list-projects>

    </div>

</template>