<script setup>

    import { storeToRefs } from 'pinia'
    import { useArticleStore } from '../store/articles'

    const { articles, loading, error } = storeToRefs(useArticleStore())

    const { fetchArticles } = useArticleStore()

    fetchArticles()

</script>

<template>
    <main>
        <div v-if="loading">loading</div>

        <div v-if="error">{{  error.message }}</div>

        <div v-if="articles" class="index">
            <li 
                v-for="article in articles"
                :key="article.id"
            >

                <RouterLink :to="`/article/${article.slug}`">{{ article.title }}</RouterLink>

                <p>Author: {{ article.author.name }}</p>

                <p>Resume: {{ article.resume }}</p>

            </li>
        </div>

    </main>
</template>