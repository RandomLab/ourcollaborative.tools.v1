<script setup>
    
    import { useRoute } from 'vue-router'

    import { storeToRefs } from 'pinia'

    import { formatDate } from '../mixins/formatDateMixin'

    import { useProjetStore } from '../store/projects'

    const { projects, loading, error } = storeToRefs(useProjetStore())

    const { fetchProjetsEnvironnement } = useProjetStore()

    const route = useRoute()

    fetchProjetsEnvironnement(route.params.name)

</script>

<template>
    <main>

        <div v-if="loading">loading</div>

        <div v-if="error">{{  error.message }}</div>
        
        <div v-if="projects" class="project">

            <div
                v-for="project in projects"
                :key="project.id"
                class="project--item"
            >
            
                    <h2>project</h2>
                    <h1><RouterLink :to="`/project/${project.slug}`">
                        {{ project.title }}</RouterLink>
                    </h1>
                

                    <h2 v-if="!project.no_date">Creation</h2>
                    <p v-if="!project.no_date">{{ formatDate(project.date_creation) }}</p>
                    
                    <h2>{{ project.author.group ? "Collectif" : "Author" }} </h2>
                    <p><RouterLink :to="`/author/${project.author.slug}`">
                        {{ project.author.group ? null : project.author.firstname }} {{ project.author.name }}
                    </RouterLink></p>

                    <h2>Description</h2>
                    <p class="description">{{ project.description }}</p>

                    <svg viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
                        <line x1="0" y1="5" x2="10" y2="5" />
                    </svg>
            </div>
            
        </div>
     </main>
</template>