import { createApp } from 'vue'
import { createPinia } from 'pinia'

import axios from 'axios'

import router from './router'
import App from './App.vue'

axios.defaults.baseURL = import.meta.env.VITE_API_ENDPOINT

import './assets/main.css'

import Header from './components/Header.vue'

const pinia = createPinia()
const app = createApp(App)

app.component('Header', Header)

app.use(pinia)

app.use(router)
    
app.mount('#app')