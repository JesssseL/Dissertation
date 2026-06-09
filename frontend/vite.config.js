import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],

  preview: {
    host: '0.0.0.0',
    port: 8080,
    allowedHosts: [
      'dissfrontend-efcvgme6e4e4agav.germanywestcentral-01.azurewebsites.net'
    ]
  },

  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
