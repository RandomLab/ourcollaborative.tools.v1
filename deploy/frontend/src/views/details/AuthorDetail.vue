<script setup>

    import { useRoute } from 'vue-router'

    import { storeToRefs } from 'pinia'
    import { useAuthorStore } from '../../store/authors'

    import AuthorProjects from '../../components/AuthorProjects.vue'

    import { cleanURL } from '../../mixins/cleanURL'

    const route = useRoute()

    const { author, loading, error } = storeToRefs(useAuthorStore())
    const { fetchAuthorBySlug } = useAuthorStore()

    fetchAuthorBySlug(route.params.slug)

</script>

<template>

    <main>
        <p v-if="loading">Loading post...</p>
        <p v-if="error">{{ error.message }}</p>
        <div 
            v-if="author"
            class="author"
        >
            <div class="author-header">
                <h1>{{ author.firstname ? author.firstname : null }} {{ author.name }}</h1>
                <p class="description">
                    {{ author.bio }}
                </p>
                <h2 v-if="author.url">Link</h2>
                <p v-if="author.url"><a :href="author.url">{{ cleanURL(author.url) }}</a></p>
            </div>
            <AuthorProjects :id="author.id" />

        </div>

    </main>
    
</template>