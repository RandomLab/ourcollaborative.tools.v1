<script setup>

    import { ref, reactive, computed, onMounted, watchEffect } from 'vue'

    import { useRoute } from 'vue-router'
    import { storeToRefs } from 'pinia'

    import { cleanURL } from '../../mixins/cleanURL'
    
    import { useAuthorStore } from '../../store/authors'

    import AuthorListProjects from './AuthorListProjects.vue'

    const route = useRoute()

    const { author, loading, error } = storeToRefs(useAuthorStore())
    
    const { fetchAuthorBySlug } = useAuthorStore()

    onMounted(() => {
        fetchAuthorBySlug(route.params.slug)
    })

    watchEffect(() => {
        fetchAuthorBySlug(route.params.slug)
    })
    
</script>

<template>
    <p v-if="loading">Loading post...</p>
    <p v-if="error">{{ error.message }}</p>
    <div
        v-if="author"
        class="author--detail"
    >   
        <h2>{{ author.group ? "Collectif" : "Author" }} </h2>
        <h1>{{ author.group ? null : author.firstname }} {{ author.name }}</h1>

        <h2 v-if="author.url">Link</h2>
        <p v-if="author.url"><a :href="author.url">{{ cleanURL(author.url) }}</a></p>

        <h2>Biography</h2>
        <p>{{ author.bio }}</p>

        <div class="ref">projets</div>

        <author-list-projects :id="author.id"></author-list-projects>

    </div>
</template>