<script setup>

    import { useRoute } from 'vue-router'
    import { storeToRefs } from 'pinia'

    import { useArticleStore } from '../../store/articles'

    const route = useRoute()

    const { article, loading, error } = storeToRefs(useArticleStore())
    
    const { fetchOneArticle } = useArticleStore()

    fetchOneArticle(route.params.slug)

</script>

<template>

    <main>
        <p v-if="loading">Loading post...</p>
        <p v-if="error">{{ error.message }}</p>
        <p v-if="article">
            
            <h1>{{ article.title }}</h1>
            <p>{{ article.author.name }}</p>
            <p>{{  article.content }}</p>
            <p>notion:
                <li
                    v-for="notion in article.notion"
                    :key="notion.id"
                >
                    <RouterLink :to="`/notion/${notion.id}`">{{ notion.title }}</RouterLink>
                </li>
            </p>
        </p>
    </main>

</template>