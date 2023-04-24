<script setup>

    import { storeToRefs } from 'pinia'
    import { useArticleStore } from '../store/articles'

    import { formatDate } from '../mixins/formatDateMixin'

    const { articles, loading, error } = storeToRefs(useArticleStore())

    const { fetchArticles } = useArticleStore()

    fetchArticles()

</script>

<template>
    <main>
        <div v-if="loading">loading</div>

        <div v-if="error">{{  error.message }}</div>

        <div 
            v-if="articles" 
            class="article--container"
        >

            <div 
                v-for="article in articles"
                :key="article.id"
                class="article--item"
            >   
                <div class="date">Add on {{ formatDate(article.date_pub, true) }}</div>

                <h2>article</h2>

                <h1><RouterLink :to="`/article/${article.slug}`">{{ article.title }}</RouterLink></h1>

                <h2>Author(s)</h2>
                <p
                    v-for="author in article.author"
                    :key="author.id"
                >
                    <RouterLink :to="`/author/${author.slug}`">{{ author.group ? null : author.firstname }} {{ author.name }}</RouterLink>
                </p>

                <h2>Resume</h2>
                <p>{{ article.resume }}</p>

                <svg height="10" width="20">
                    <line x1="0" y1="0" x2="20" y2="0"/>            
                </svg> 

            </div>
        
        </div>

    </main>
</template>

<style scoped>

    line {
        stroke: var(--second-color);
        stroke-width: 2;
    }
    
</style>