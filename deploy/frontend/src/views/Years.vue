<script setup>
    
    import { useRoute } from 'vue-router'

    import { storeToRefs } from 'pinia'

    import { formatDate } from '../mixins/formatDateMixin'

    import { useProjetStore } from '../store/projects'

    import IndexProject from '../components/project/IndexProject.vue'

    import Filtres from '../components/utils/Filtres.vue'


    const { projects, loading, error } = storeToRefs(useProjetStore())

    const { fetchProjetsYear } = useProjetStore()

    const route = useRoute()

    fetchProjetsYear(route.params.year)

</script>

<template>
    <main>

        <div v-if="loading">loading</div>

        <div v-if="error">{{  error.message }}</div>

        
        <div 
            v-if="projects.length" 
            class="project-index"
        >

            <div
                v-for="project in projects"
                :key="project.id"
                class="project--item"
            >
                <index-project 
                    :project="project" 
                    :id="project.id">
                </index-project>

            </div>
            
        </div>
        <div 
            v-else
            class="lettrine"
        >
            <h1>No projects found</h1>
        </div>
    </main>
</template>