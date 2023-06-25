<script setup>

    import { marked } from 'marked'

    const props = defineProps(['result'])

</script>


<template>
    <div class="search-result--item">

        <svg height="10" width="20">
            <line x1="0" y1="0" x2="20" y2="0"/>            
        </svg> 

        <h2>{{ result.type }}</h2>

        <!-- project -->
        
        <h1 v-if="result.type === 'project'"><RouterLink :to="`/project/${result.slug}`">{{ result.title }}</RouterLink></h1>
        
        <h2 v-if="result.type === 'project'">usage
        <span><RouterLink :to="`/usage/${result.usage}`">{{ result.usage }}</RouterLink></span></h2>
        
        <h2 v-if="result.type === 'project'">description</h2>
        
        <p v-if="result.type === 'project'" v-html="marked.parse(result.description)"></p>

        <!-- notion -->

        <h1 v-if="result.type === 'notion'"><RouterLink :to="`/notion/${result.slug}`">{{ result.title }}</RouterLink></h1>
        
        <h2 v-if="result.type === 'notion'">content</h2>
        
        <p v-if="result.type === 'notion'" v-html="marked.parse(result.content)"></p>

        <!-- auteur -->

        <h1 v-if="result.type === 'author'"><RouterLink :to="`/author/${result.slug}`">{{ result.group ? null : result.firstname  }} {{ result.name }}</RouterLink></h1>

        <h2 v-if="result.type === 'author'">biography</h2>
        
        <p v-if="result.type === 'author'" v-html="marked.parse(result.bio)"></p>

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