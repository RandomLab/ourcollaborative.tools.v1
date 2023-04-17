import axios from "axios"

import { defineStore } from "pinia"

export const useReferenceStore = defineStore({
    id:"references",
    state: () => ({
        references: [],
        loading: null,
        error: null
    }),
    actions: {

       
        async fetchReferences() {
            this.references = []
            this.loading = true
            try {
                this.references = await axios
                                    .get(`reference/`)
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