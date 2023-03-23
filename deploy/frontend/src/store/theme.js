import axios from "axios"

import { defineStore } from "pinia"


export const useThemeStore = defineStore({
    id:"theme",
    state: () => ({
        isDark: true
    }),
    getters: {
    },
    actions: {
        setTheme() {
            // console.log('set')
            this.isDark = !this.isDark
        }
    }
})