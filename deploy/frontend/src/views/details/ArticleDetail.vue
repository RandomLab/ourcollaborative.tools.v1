<script setup>

    import { useRoute } from 'vue-router'
    import { storeToRefs } from 'pinia'

    import { marked } from 'marked'


    // const renderer = {
        // heading(text, level) {
        //     const escapedText = text.toLowerCase().replace(/[^\w]+/g, '-')
        //     return `
        //         <h${level}>
        //             test ${text}
        //         </h${level}>
        //     `
        // }
    //     paragraph(text) {
    //         const escapedText = text.toLowerCase().replace(/\[.*?\]/g, `<div class="note">foot</div>`)
    //         return `
    //             <p> 
    //             ${text}
    //                 ${escapedText}
    //             </p>
    //         `
    //     }
    // }   

    // marked.use({ renderer })

    // marked.use({
    //     renderer: new marked.Renderer(),
    //     gfm: true,
    //     tables: true,
    //     extra: true,
    //     breaks: false,
    //     pedantic: false,
    //     sanitize: false,
    //     smartLists: true,
    //     smartypants: false
    // })

    import { useArticleStore } from '../../store/articles'

    const route = useRoute()

    const { article, loading, error } = storeToRefs(useArticleStore())
    
    const { fetchOneArticle } = useArticleStore()

    fetchOneArticle(route.params.slug)

</script>

<template>

    <main>
        
        <div class="loading" v-if="loading">Loading article</div>
        <div class="error" v-if="error">{{ error.message }}</div>

        <div 
            v-if="article"
            class="article--container"
        >

            <div class="article--detail">

                <div class="article--text">

                    <h2>article</h2>

                    <h1>{{ article.title }}</h1>

                    <h2>Author(s)</h2>
                    <p
                        v-for="author in article.author"
                        :key="author.id"
                    ><RouterLink :to="`/author/${author.slug}`">{{ author.group ? null : author.firstname }} {{ author.name }}</RouterLink></p>

                    <div 
                        class="article--content"
                        v-html="marked.parse(article.content)"
                    >
                    </div>

                </div>

                <div class="article--notions">
                    <li 
                        v-for="notion in article.notion"
                        :key="notion.id"
                    >
                        <h2><RouterLink :to="`/notion/${notion.slug}`">{{ notion.title }}</RouterLink></h2>
                        <p v-html="marked.parse(notion.content)"></p>
                    </li>
                </div>
            
            </div>

        </div>
    </main>

</template>