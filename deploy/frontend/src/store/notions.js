import axios from "axios"

import { defineStore } from "pinia"

export const useNotionStore = defineStore({
    id:"notion",
    state: () => ({
        notions: [],
        notion: null,
        loading: false,
        error: null
    }),
    actions: {
        async fetchNotions() {
            this.notions = []
            this.loading = true

            try {
                this.notions = await axios
                                        .get('notion/')
                                        .then((response) => {
                                            return response.data
                                        })
            } catch (error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async fetchNotionBySlug(slug) {
            this.notion = null
            this.loading = true

            try {
                this.notion = await axios
                                        .get(`notion/${slug}`)
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