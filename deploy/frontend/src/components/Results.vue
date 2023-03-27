<script setup>

     const props = defineProps(['result'])

</script>


<template>
    <div class="search-result--projet">

        <svg height="10" width="20">
            <line x1="0" y1="0" x2="20" y2="0"/>            
        </svg> 

        <h2>{{ result.type }}</h2>
        <h1><RouterLink :to="result.type === 'project' ? `/project/${result.slug}` : `/notion/${result.slug}`">{{ result.title }}</RouterLink></h1>
        <h2 v-if="result.type === 'project'">{{ result.author.group ? "Collectif" : "Author" }}
        <span><RouterLink :to="`/author/${result.author.slug}`">{{ result.author.group ? null : result.author.firstname }} {{ result.author.name }}</RouterLink></span></h2>
        <h2 v-if="result.type === 'project'">usage
        <span><RouterLink :to="`/usage/${result.usage}`">{{ result.usage }}</RouterLink></span></h2>
        <h2 v-if="result.type === 'project'">description</h2>
        <p v-if="result.type === 'project'">{{ result.description }}</p>
        <h2 v-if="result.type === 'notion'">content</h2>
        <p v-if="result.type === 'notion'">{{ result.content }}</p>

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