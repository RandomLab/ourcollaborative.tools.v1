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
        async filterEnvProjects(env) {
            this.projects = []
            this.loading = true
            try {
                this.projects = await axios
                                        .get('project/')
                                        .then((response) => {
                                            return response.data.filter((project) => {
                                                return project.environnement === env
                                            })
                                        })

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async filterUsageProjects(usage) {
            this.projects = []
            this.loading = true
            try {
                this.projects = await axios
                                        .get('project/')
                                        .then((response) => {
                                            return response.data.filter((project) => {
                                                return project.usage === usage
                                            })
                                        })

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async filterTemporalityProjects(temporality) {
            this.projects = []
            this.loading = true
            try {
                this.projects = await axios
                                        .get('project/')
                                        .then((response) => {
                                            return response.data.filter((project) => {
                                                return project.temporality === temporality
                                            })
                                        })

            } catch(error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
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
        async fetchProjetsEnvironnement(environnement) {
            this.projects = []
            this.loading = true

            try {
                this.projects = await axios
                                        .get(`projects_by_environnement/${environnement}`)
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
        }
    }
})