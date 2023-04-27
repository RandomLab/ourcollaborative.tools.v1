<script setup>

    import { computed } from 'vue'

    import { useRoute } from 'vue-router'
    import { storeToRefs } from 'pinia'
    import { marked } from 'marked'

    import { formatDate } from '../../mixins/formatDateMixin'
    import { cleanURL } from '../../mixins/cleanURL'

    import ProjectImages from '../../components/project/ProjectImages.vue'
    import ProjectNotions from '../../components/project/ProjectNotions.vue'

    import { useProjetStore } from '../../store/projects'

    const route = useRoute()

    const { project, loading, error } = storeToRefs(useProjetStore())
    
    const { fetchOneProjet } = useProjetStore()

    fetchOneProjet(route.params.slug)

    function setWordToLower(word) {
        return word.toLowerCase()
    }

</script>

<template>

    <main>

        <div class="loading" v-if="loading">Loading project</div>
        
        <div class="error" v-if="error">{{ error.message }}</div>

        <div v-if="project" class="project">
            
            <div class="project--informations">
                
                <div class="project-informations--header">
               
                    <h2>project</h2>
                    <h1>{{ project.title }}</h1>
               
                </div>

                <div class="project-informations--details">
                    
                    <div class="project-informations-details--left">

                        <h2>Description</h2>
                        <p class="description" v-html="marked.parse(project.description)"></p>
                        
                        <h2 v-if="!project.no_date">Creation</h2>
                        <p v-if="!project.no_date">
                            <RouterLink :to="`/year/${formatDate(project.date_creation)}`">{{ formatDate(project.date_creation) }}</RouterLink>
                        </p>

                        <h2>Author(s)</h2>
                        <p
                            v-for="author in project.author"
                            :key="author.id"
                        >   
                            
                        <RouterLink :to="`/author/${author.slug}`">
                            {{ author.group ? null : author.firstname }} {{ author.name }}
                        </RouterLink>
                        </p>


                        <h2 v-if="project.url">Link</h2>
                        <p v-if="project.url"><a :href="project.url">{{ cleanURL(project.url) }}</a></p>

                    </div>

                    <div class="project-informations-details--right">
                        
                        <h2 v-if="project.usage">Usage</h2>
                        <p v-if="project.usage">
                            <RouterLink :to="`/usage/${setWordToLower(project.usage)}`">{{ project.usage }}</RouterLink>
                        </p>

                        <h2 v-if="project.temporality">Temporality</h2>
                        <p v-if="project.temporality">
                            <RouterLink :to="`/temporality/${setWordToLower(project.temporality)}`">{{ project.temporality }}</RouterLink>
                        </p>

                        <h2 v-if="project.environment">Technical Environnement</h2>
                        <p v-if="project.environment">
                            <RouterLink :to="`/environment/${setWordToLower(project.environment)}`">{{ project.environment }}</RouterLink>
                        </p>
                        
                        <h2 v-if="project.licence">Licence</h2>
                        <p v-if="project.licence">
                            {{ project.licence.title }}
                            <!-- <RouterLink :to="`/licence/${project.licence.slug}`">{{ project.licence.title }}</RouterLink> -->
                        </p>
                        
                        <h2 v-if="project.notion">Notions</h2>
                        <li
                            v-for="notion in project.notion"
                            :key="notion.id"
                        >
                            <RouterLink :to="`/notion/${notion.slug}`">{{ notion.title }}</RouterLink>
                        </li>                        
                    </div>

                </div>
                        
           
            
            </div>

            <project-images :id="project.id" ></project-images>

            <project-notions :notions="project.notion"></project-notions>


        </div>
    </main>

</template>