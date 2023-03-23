<script setup>

    import { useRoute } from 'vue-router'

    import { storeToRefs } from 'pinia'
    
    import { useNotionStore } from '../../store/notions'

    import NotionProjects from '../../components/notion/NotionListProjects.vue'

    const route = useRoute()

    const { notion, loading, error } = storeToRefs(useNotionStore())

    const { fetchNotionBySlug } = useNotionStore()

    fetchNotionBySlug(route.params.slug)

</script>

<template>

    <main>
        
        <p v-if="loading">Loading post...</p>
        
        <p v-if="error">{{ error.message }}</p>
        
        <div 
            v-if="notion"
            class="notion"
        >
            <div class="notion-header">
                <h1>{{ notion.title }}</h1>
                <p class="description">
                    {{  notion.content }}
                </p>
            </div>

            <NotionProjects :id="notion.id" />

        </div>

    </main>

</template>