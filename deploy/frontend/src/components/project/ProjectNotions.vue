<script setup>

    import { marked } from 'marked'

    const props = defineProps(['notions'])

</script>

<template>
    
    <div 
        class="project-informations--notions"
    >
        <div class="ref">notions</div>

        <div class="project-notion">

            <div
                v-for="notion in notions"
                :key="notion.id"
                class="project-notion--item"
            >
                <h2 v-if="notion.publish"><RouterLink :to="`/notion/${notion.slug}`">{{ notion.title }}</RouterLink></h2>
                <p v-if="notion.publish" v-html="marked.parse(notion.content)"></p>

            </div>

        </div>


    </div>

</template>
