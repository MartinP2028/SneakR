// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/supabase', '@nuxt/ui', '@nuxtjs/tailwindcss'],
  supabase: {
    redirectOptions: {
      login: '/login',
      callback: '/',
      exclude: ['/', "/login", "/register", "/confirm", "/details/*", "/forgot_password", "/update_password"],
    }
  },
})
