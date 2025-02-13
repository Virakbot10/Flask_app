import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  server: {
    host: '0.0.0.0',
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, '')
      },
    },
  },
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': path.resolve(fileURLToPath(new URL('.', import.meta.url)), 'src')
    },
  },
})
