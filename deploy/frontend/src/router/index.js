import { 
    createRouter,
    createWebHistory
} from 'vue-router'

// import Home from '../views/Home.vue'

import Projects from '../views/Projects.vue'
import Project from '../views/details/ProjectDetail.vue'

import Years from '../views/Years.vue'

import Articles from '../views/Articles.vue'
import ArticleDetail from '../views/details/ArticleDetail.vue'

import Notions from '../views/Notions.vue'
import NotionDetail from '../views/details/NotionDetail.vue'

import LicenceDetail from '../views/details/LicenceDetail.vue'

import Authors from '../views/Authors.vue'
import AuthorDetail from '../views/details/AuthorDetail.vue'

import Informations from '../views/Informations.vue'

import Search from '../views/Search.vue'

import Usages from '../views/Usages.vue'
import Temporalities from '../views/Temporalities.vue'
import Environnements from '../views/Environnements.vue'

import Mediagraphy from '../views/Mediagraphy.vue'

import PageNotFound from '../views/PageNotFound.vue'

const routes = [
    // {
    //     path: '/',
    //     name: 'home',
    //     component: Home,
    // },
    {
        path: '/',
        name: 'projects',
        component: Projects

    },
    {
        path: '/year/:year',
        name: 'year',
        component: Years
    },
    {
        path: '/project/:slug',
        name: 'project',
        component: Project
    },
    {
        path: '/articles',
        name: 'articles',
        component: Articles
    },
    {
        path: '/article/:slug',
        name: 'article',
        component: ArticleDetail
    },
    {
        path: '/notions',
        name: 'notions',
        component: Notions
    },
    {
        path: '/notion/:slug',
        name: 'notion',
        component: NotionDetail
    },
    {
        path: '/licence/:slug',
        name: 'licence',
        component: LicenceDetail
    },
    {
        path: '/usage/:name',
        name: 'usage',
        component: Usages
    },
    {
        path: '/temporality/:name',
        name: 'temporality',
        component: Temporalities
    },
    {
        path: '/environment/:name',
        name: 'environment',
        component: Environnements
    },
    {
        path: '/authors',
        name: 'authors',
        component: Authors
    },
    {
        path: '/author/:slug',
        name: 'author',
        component: AuthorDetail
    },
    {
        path:'/mediagraphy',
        name: 'mediagraphy',
        component: Mediagraphy
    },
    {
        path: '/about',
        name: 'informations',
        component: Informations
    },
    {
        path: '/search',
        name: 'search',
        component: Search
    },
    {
        path: '/:pathMatch(.*)*',
        component: PageNotFound,
    }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})


export default router