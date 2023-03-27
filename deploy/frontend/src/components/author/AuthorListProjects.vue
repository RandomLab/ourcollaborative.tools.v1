<script setup>
    import  { onMounted, computed } from 'vue'

    import { useRoute } from 'vue-router'
   
    import { storeToRefs } from 'pinia'

    import { useProjetStore } from '../../store/projects'
    
    const props = defineProps(['id'])
    
    const { projects, loading, error } = storeToRefs(useProjetStore())

    const { fetchProjetsAuthor } = useProjetStore()

    onMounted(() => {
        fetchProjetsAuthor(props.id)
    })


</script>

<template>
    <p v-if="loading">Loading post...</p>
    <p v-if="error">{{ error.message }}</p>

    <div 
      v-if="projects.length > 0"
      class="author-projects"
    >
         <div
            v-for="project in projects"
            :key="project.id"
            class="author-projects--item"
            > 
            
            <h2>project</h2>
            <h1><RouterLink :to="`/project/${project.slug}`">{{ project.title }}</RouterLink></h1>
            <h2>{{ project.author.group ? "Collectif" : "Author" }}
            <span>{{ project.author.group ? null : project.author.firstname }} {{ project.author.name }}</span></h2>
            <h2>description</h2>
            <p>{{ project.description }}</p>

            <svg height="10" width="20">
                <line x1="0" y1="0" x2="20" y2="0"/>            
            </svg> 
        
        </div>

    </div>

</template>

<style scoped>
    
    svg {   
        margin-top: 25px;
    }   

    line {
        stroke: var(--second-color);
        stroke-width: 2;
    }
</style>