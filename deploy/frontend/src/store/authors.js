import axios from "axios"

import { defineStore } from "pinia"

export const useAuthorStore = defineStore({
    id:"author",
    state: () => ({
        authors: [],
        author: null,
        loading: null,
        error: null
    }),
    actions: {

        setAuthor(obj) {
            this.author = obj
        },

        async fetchAuthors() {
            this.authors = []
            this.loading = true
            try {
                this.authors = await axios
                                    .get(`author/`)
                                    .then((response) => {
                                        return response.data
                                    })
            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async fetchAuthorBySlug(slug) {
            this.author = null
            this.loading = true
            try {
                this.author = await axios
                                    .get(`author/${slug}`)
                                    .then((response) => {
                                        return response.data
                                    })
            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        }

    }
})