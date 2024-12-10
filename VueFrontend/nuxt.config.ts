// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  devServer: {
    host: "0.0.0.0",
    port: 5173, // you can replace this port with any port
  },

  vite: {
    server: {
      hmr: {
        protocol: 'ws',
        host: '0.0.0.0',  
      }
    }
  },

  app: {
    head: {
      title: 'Resume Builder',
      meta: [
        {name: 'description', content: 'ATS friendly resume'}
      ],
      link: [
        {rel: 'stylesheet', href: 'https://fonts.googleapis.com/icon?family=Material+Icons'},
      ],
      script: [
        {
          src: 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js'
        },
      ]
    }
  },

  css: ['~/assets/css/main.css', '~/assets/scss/styles.scss'],

  runtimeConfig: {
    public: {
      BASE_URL: process.env.BASE_URL
    }
  },
  plugins: [
    '~/plugins/useAxios.ts',
  ],

  compatibilityDate: '2024-10-06'
})