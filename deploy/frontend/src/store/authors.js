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
    getters: {
        // getAuthorById: (state) => {
        //     return (authorId) => {
        //         const author =  state.authors.find((author) => {
        //             return author.id === authorId
        //         })
        //         return author
        //     }
        // }    
    },
    actions: {
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