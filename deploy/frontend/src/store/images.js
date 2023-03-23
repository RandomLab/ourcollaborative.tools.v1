import axios from "axios"

import { defineStore } from "pinia"

export const useImagesStore = defineStore({
    id:"images",
    state: () => ({
        images: [],
        image: null,
        loading: false,
        error: null
    }),
    actions: {
        async fetchOneImage(object_id) {
            console.log(object_id)
            this.image = null
            this.loading = true

            try {
                this.image = await axios
                                        .get(`image_project/${object_id}/`)
                                        .then((response) => {
                                            console.log(response.data[0])
                                            return response.data[0]
                                        })
            } catch (error) {
                this.error = error
            } finally {
                this.loading = false
            }

        },
        async fetchImages() {
            this.images = []
            this.loading = true

            try {
                this.images = await axios
                                        .get(`images`)
                                        .then((response) => {
                                            return response.data
                                        })
            } catch (error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async fetchImagesProject(object_id) {
            this.images = []
            this.loading = true

            try {
                this.images = await axios
                                        .get(`image_project/${object_id}/`)
                                        .then((response) => {
                                            return response.data
                                        })
            } catch (error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
    }
})