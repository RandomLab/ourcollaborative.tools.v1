import axios from "axios"

import { defineStore } from "pinia"

export const useProjetStore = defineStore({
    id:"project",
    state: () => ({
        projects: [],
        project: null,
        loading: false,
        error: null,
    }),
    actions: {
        
        /*--------------------*/
        /* data
        /*--------------------*/
        
        async fetchProjets() {
            this.projects = []
            this.loading = true

            try {
                this.projects = await axios
                                        .get('project/')
                                        .then((response) => {
                                            return response.data
                                        })
                

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async fetchOneProjet(slug) {
            this.project = null
            this.loading = true

            try {
                this.project = await axios
                                        .get(`project/${slug}`)
                                        .then((response) => {
                                            return response.data
                                        })
            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },

        async fetchProjetsAuthor(authorId) {
            this.projects = []
            this.loading = true

            try {
                this.projects = await axios
                                        .get(`projects_by_author/${authorId}`)
                                        .then((response) => {
                                            return response.data
                                        })
                

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },

        /*--------------------*/
        /* tri
        /*--------------------*/

        triAlpha(direction) {
            if (direction === 'asc') {
                this.projects.sort((a, b) => {
                        
                    if (a.title.toLowerCase() < b.title.toLowerCase()) {
                        return -1
                    }
    
                    if (a.title.toLowerCase() > b.title.toLowerCase()) {
                        return 1
                    }
                    return 0
    
                })
            } else {
                this.projects.reverse((a, b) => {
                        
                    if (a.title.toLowerCase() < b.title.toLowerCase()) {
                        return -1
                    }
    
                    if (a.title.toLowerCase() > b.title.toLowerCase()) {
                        return 1
                    }
                    return 0
    
                })
            }
        },

        /*--------------------*/
        /* filres Client
        /*--------------------*/
        
        // filterBy() {
        //     this.projects = this.projects.filter((item) => {
        //         return item.temporality === 'continuous'
        //     })
        //     console.log(this.projects)
        // },

        /*--------------------*/
        /* filres API
        /*--------------------*/


        async fetchProjetsEnvironnement(environment) {
            this.projects = []
            this.loading = true

            try {
                this.projects = await axios
                                        .get(`projects_by_environment/${environment}`)
                                        .then((response) => {
                                            return response.data
                                        })
                

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async fetchProjetsTemporality(temporality) {
            this.projects = []
            this.loading = true

            try {
                this.projects = await axios
                                        .get(`projects_by_temporality/${temporality}`)
                                        .then((response) => {
                                            return response.data
                                        })
                

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async fetchProjetsUsage(usage) {
            this.projects = []
            this.loading = true

            try {
                this.projects = await axios
                                        .get(`projects_by_usage/${usage}`)
                                        .then((response) => {
                                            return response.data
                                        })
                

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async fetchProjetsNotion(notionId) {
            this.projects = []
            this.loading = true

            try {
                this.projects = await axios
                                        .get(`projects_by_notion/${notionId}`)
                                        .then((response) => {
                                            return response.data
                                        })
                

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },

        async fetchProjetsYear(year) {
            this.projects = []
            this.loading = true

            try {
                this.projects = await axios
                                        .get(`projects_by_year/${year}`)
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