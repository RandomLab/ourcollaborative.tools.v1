import axios from "axios"

import { defineStore } from "pinia"


export const useSearchStore = defineStore({
    id:"search",
    state: () => ({
        results: [],
        loading: false,
        error: null
    }),
    getters: {
    },
    actions: {
        async fetchSearch(words, type) {
            this.results = []
            this.loading = true

            try {
                this.results = await axios
                                        .get(`search_${type}/?search=${words}`)
                                        .then((response) => {
                                            return response.data
                                        })
                

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
    }
})