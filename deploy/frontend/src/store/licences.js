import axios from "axios"

import { defineStore } from "pinia"

export const useLicenceStore = defineStore({
    id: "licence",
    state: () => ({
        licence: null,
        loading: false,
        error: null
    }),
    actions: {
        async fetchLicenceBySlug(slug) {
            this.licence = null
            this.loading = true

            try {
                this.licence = await axios
                                        .get(`licence/${slug}`)
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