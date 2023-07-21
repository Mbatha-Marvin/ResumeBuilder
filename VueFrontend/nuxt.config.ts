// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true }, 
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
})
