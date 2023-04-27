<script setup>

    import { ref, reactive, computed, onMounted } from 'vue'
    
    import { storeToRefs } from 'pinia'

    import { formatDate } from '../mixins/formatDateMixin'

    import { useProjetStore } from '../store/projects'

    import IndexProject from '../components/project/IndexProject.vue'

    import Filtres from '../components/utils/Filtres.vue'

    const { projects, loading, error } = storeToRefs(useProjetStore())

    const { fetchProjets, triAlpha, triDate } = useProjetStore()

    onMounted(() => {
        fetchProjets()
    })

    const state = reactive({
            type: null,
            name: null
        })

    function setState(newState) {

        state.type = newState.type
        state.name = newState.name

        if (state.type === 'alpha') {
            triAlpha()
        }

        if (state.type === 'date') {
            triDate()
        }

    }

    function filteredProjects(projects) {

        if (state.type === 'temporality') {
            return state.type === null ? projects : projects.filter((project) => {
                return project.temporality === state.name
            })
        } else if (state.type === 'usage') {
            return state.type === null ? projects : projects.filter((project) => {
                return project.usage === state.name
            })
        } else if (state.type === 'environment') {
            return state.type === null ? projects : projects.filter((project) => {
                return project.environment === state.name
            })
        } else {
            return projects
        }
    }
  
</script>

<template>
    
      <main>

        <div class="loading" v-if="loading">Loading projects</div>
        
        <div class="error" v-if="error">{{ error.message }}</div>

        <div class="filters">
            <button @click="setState({ type: 'alpha', name: null })">title</button>

            <button @click="setState({ type: 'date', name: null })">date</button>
            
            <!-- <button @click="setState({ type: 'temporality', name: 'event'})">event</button>
            <button @click="setState({ type: 'temporality', name: 'continuous'})">continuous</button>

            <button @click="setState({ type: 'usage', name: 'collaboration'})">collaboration</button>
            <button @click="setState({ type: 'usage', name: 'contribution'})">contribution</button>
            <button @click="setState({ type: 'usage', name: 'participatory'})">participatory</button>

            <button @click="setState({ type: 'environment', name: 'web'})">web</button>
            <button @click="setState({ type: 'environment', name: 'desktop'})">desktop</button>
            <button @click="setState({ type: 'environment', name: 'mobile'})">mobile</button> -->
        
        </div>

        <div v-if="projects" class="project-index">

            <div
                v-for="project in filteredProjects(projects)"
                :key="project.id"
                class="project--item"
            >   
                            
                <index-project 
                    :project="project" 
                    :id="project.id">
                </index-project>

            </div>
            
        </div>
        <div v-else><h2>Pas de projets</h2></div>
    </main>
        
</template>

<style scoped>
   
</style>