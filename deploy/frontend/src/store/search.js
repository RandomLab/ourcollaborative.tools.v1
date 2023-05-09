import axios from "axios"

import { defineStore } from "pinia"


export const useSearchStore = defineStore({
    id:"search",
    state: () => ({
        notions: [],
        projects: [],
        authors: [],
        results: [],
        loading: false,
        error: null
    }),
    getters: {
        mergeData(state) {
            return state.results = [...state.notions, ...state.authors, ...state.projects]
        }
    },
    actions: {
        async fetchNotions(words) {
            this.notions = []
            this.loading = true

            try {
                this.notions = await axios
                                        .get(`search_notions/?search=${words}`)
                                        .then((response) => {
                                            return response.data
                                        })
                

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async fetchProjects(words) {
            this.projects = []
            this.loading = true

            try {
                this.projects = await axios
                                        .get(`search_projects/?search=${words}`)
                                        .then((response) => {
                                            return response.data
                                        })
                

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async fetchAuthors(words) {
            this.authors = []
            this.loading = true

            try {
                this.authors = await axios
                                        .get(`search_authors/?search=${words}`)
                                        .then((response) => {
                                            return response.data
                                        })
                

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
      
        async fetchSearch(words) {
            this.loading = true
            try {
                this.fetchNotions(words)
                this.fetchProjects(words)
                this.fetchAuthors(words)
            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        }
    }
})