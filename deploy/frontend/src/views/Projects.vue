<script setup>

    import { ref } from 'vue'
    
    import { storeToRefs } from 'pinia'

    import { formatDate } from '../mixins/formatDateMixin'

    import { useProjetStore } from '../store/projects'

    const { projects, loading, error } = storeToRefs(useProjetStore())

    const { fetchProjets, filterTemporalityProjects, filterUsageProjects, filterEnvProjects } = useProjetStore()

    fetchProjets()

    import IndexProject from '../components/project/IndexProject.vue'

    const selectedTemporality = ref("Temporality")
    const selectedUsage = ref("Usage")
    const selectedEnv = ref("Environnement")

    function changeTemporality(e) {
        if (selectedTemporality.value === "Temporality") {
            fetchProjets()
        } else {
            filterTemporalityProjects(selectedTemporality.value)
        }
    }

    function changeUsage(e) {
        if (selectedUsage.value === "Usage") {
            fetchProjets()
        } else {
            filterUsageProjects(selectedUsage.value)
        }
    }

    function changeEnv(e) {
        if (selectedEnv.value === "Environnement") {
            fetchProjets()
        } else {
            filterEnvProjects(selectedEnv.value)
        }
    }
    
</script>

<template>
    
      <main>

        <div v-if="loading">loading</div>

        <div v-if="error">{{  error.message }}</div>
        
        <div v-if="projects" class="project-index">

            <!-- <select v-model="selectedTemporality" @change="changeTemporality">
                <option value="Temporality">Temporality</option>
                <option value="Event">Event</option>
                <option value="Continuous">Continuous</option>
            </select>

            <select v-model="selectedUsage" @change="changeUsage">
                <option value="Usage">Usage</option>
                <option value="Collaboration">Collaboration</option>
                <option value="Cooperation">Cooperation</option>
                <option value="Contribution">Contribution</option>
                <option value="Participatory">Participatory</option>
            </select>

             <select v-model="selectedEnv" @change="changeEnv">
                <option value="Environnement">Environnement</option>
                <option value="Web">Web</option>
                <option value="Desktop">Desktop</option>
                <option value="Mobile">Mobile</option>
            </select> -->

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
        <div v-else><h2>Pas de projets</h2></div>
    </main>
        
</template>