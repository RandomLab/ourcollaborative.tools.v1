import axios from "axios"

import { defineStore } from "pinia"


export const useIndexStore = defineStore({
    id:"all",
    state: () => ({
        datas: [],
        loading: false,
        error: null
    }),
    getters: {
    },
    actions: {
        async fetchAll() {
            this.datas = []
            this.loading = true

            try {
                this.datas = await axios
                                        .get('index')
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