<script setup>
    import  { onMounted, computed } from 'vue'
    import { useRoute } from 'vue-router'
    import { storeToRefs } from 'pinia'
    import { marked } from 'marked'

    import { useProjetStore } from '../../store/projects'
    
    const props = defineProps(['id'])
    
    const { projects, loading, error } = storeToRefs(useProjetStore())

    const { fetchProjetsAuthor } = useProjetStore()

    onMounted(() => {
        fetchProjetsAuthor(props.id)
    })


</script>

<template>
    <div v-if="loading">Loading projects</div>

    <div v-if="error">{{ error.message }}</div>

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
            <!-- <h2>Author(s)</h2>
            <p 
                v-for="author in project.author"
                :key="author.id"
            >{{ author.group ? null : author.firstname }} {{ author.name }}</p> -->
            <h2>description</h2>
            <p v-html="marked.parse(project.short_description ? project.short_description : project.description)"></p>

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