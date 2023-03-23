import axios from "axios"

import { defineStore } from "pinia"

export const useArticleStore = defineStore({
    id:"article",
    state: () => ({
        articles: [],
        article: null,
        loading: false,
        error: null
    }),
    actions: {
        async fetchArticles() {
            this.articles = []
            this.loading = true

            try {
                this.articles = await axios
                                        .get('article/')
                                        .then((response) => {
                                            return response.data
                                        })
            } catch (error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async fetchOneArticle(slug) {
            this.article = null
            this.loading = true

            try {
                this.article = await axios
                                        .get(`article/${slug}`)
                                        .then((response) => {
                                            return response.data
                                        })
            } catch (error) {
                this.error = error
            } finally {
                this.loading = false
            }
        }
    }
})