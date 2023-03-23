<script setup>

    import { useRoute } from 'vue-router'
   
    import { storeToRefs } from 'pinia'
    
    import { useProjetStore } from '../../store/projects'
    
    const props = defineProps(['id'])
    
    const { projects, loading, error } = storeToRefs(useProjetStore())
    
    const { fetchProjetsNotion } = useProjetStore()

    fetchProjetsNotion(props.id)

</script>

<template>
    <p v-if="loading">Loading post...</p>
    <p v-if="error">{{ error.message }}</p>
    <div 
      v-if="projects.length > 0"
      class="notion-projects"
    >

        <h2>Projects</h2>

            <div
            v-for="project in projects"
            :key="project.id"
            class="notion-projects--item"
            > 

            <RouterLink :to="`/project/${project.slug}`">{{ project.title }}</RouterLink>
            
        </div>
        
    </div>
</template>