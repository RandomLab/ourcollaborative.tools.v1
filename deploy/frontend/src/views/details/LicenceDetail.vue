<script setup>

    import { ref, reactive, computed, onMounted } from 'vue'

    import { useRoute } from 'vue-router'

    import { storeToRefs } from 'pinia'
    
    import { useLicenceStore } from '../../store/licences'

    const route = useRoute()

    const { licence, loading, error } = storeToRefs(useLicenceStore())

    const { fetchLicenceBySlug } = useLicenceStore()

    fetchLicenceBySlug(route.params.slug)

</script>

<template>

    <main>
        
        <div class="loading" v-if="loading">Loading licence</div>
        
        <div class="error" v-if="error">{{ error.message }}</div>
        
        <div 
            class="licence--container"
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