<script setup>

    import { useRoute } from 'vue-router'

    import { storeToRefs } from 'pinia'
    
    import { useLicenceStore } from '../../store/licences'

    // import NotionProjects from '../../components/NotionProjects.vue'

    const route = useRoute()

    const { licence, loading, error } = storeToRefs(useLicenceStore())

    const { fetchLicenceBySlug } = useLicenceStore()

    fetchLicenceBySlug(route.params.slug)

</script>

<template>

    <main>
        
        <p v-if="loading">Loading post...</p>
        
        <p v-if="error">{{ error.message }}</p>
        
        <div 
            v-if="licence"
            class="licence"
        >
            <div class="licence-header">
                <h1>{{ licence.title }}</h1>
                <p class="description">
                    {{  licence.content }}
                </p>
            </div>


        </div>

    </main>

</template>