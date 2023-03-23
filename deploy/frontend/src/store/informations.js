import axios from "axios"

import { defineStore } from "pinia"


export const useInformationsStore = defineStore({
    id:"informations",
    state: () => ({
        informations: [],
        loading: false,
        error: null
    }),
    getters: {
    },
    actions: {
        async fetchInformations() {
            this.informations = []
            this.loading = true

            try {
                this.informations = await axios
                                        .get('informations/')
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