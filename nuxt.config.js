export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Jobzone',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content:
          'Explore Jobzone, your trusted job search platform, free from fraudulent listings thanks to our advanced machine learning filters.',
      },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['animate.css/animate.compat.css'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [{ src: '@/plugins/aos.js', mode: 'client' }],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/tailwindcss
    '@nuxtjs/tailwindcss',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    'vue-toastification/nuxt',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: 'http://localhost:6001',
  },

  toast: {
    position: 'top-center',
    timeout: 3000,
    transition: 'Vue-Toastification__fade',
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},

  server: {
    port: 4000,
  },

  tailwindcss: {
    config: {
      plugins: [
        require('@tailwindcss/typography'),
        require('@tailwindcss/forms')({
          strategy: 'class',
        }),
        require('daisyui'),
      ],
      daisyui: {
        themes: ['corporate', 'business', 'wireframe'],
      },
    },
  },
};
