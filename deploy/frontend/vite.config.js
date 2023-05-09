import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import dns from 'dns'
import vue from '@vitejs/plugin-vue'

dns.setDefaultResultOrder('verbatim')

export default defineConfig({
  server: {
    host: true
  },
  plugins: [
    vue(),
  ],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
  }
})
