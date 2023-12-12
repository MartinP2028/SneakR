// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  colorMode: {
    preference: "light",
  },
  modules: ["@nuxtjs/supabase", "@nuxt/ui", "@nuxtjs/tailwindcss"],
  supabase: {
    redirectOptions: {
      login: "/login",
      callback: "/",
      exclude: [
        "/",
        "/login",
        "/register",
        "/confirm",
        "/details/*",
        "/forgot_password",
        "/update_password",
      ],
    },
  },
});
