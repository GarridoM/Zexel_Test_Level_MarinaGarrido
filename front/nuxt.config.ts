// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({

    devtools: { enabled: true },

    ssr: false,

    components: true,

    modules: [
        '@nuxtjs/i18n',
        '@pinia/nuxt',
        '@pinia-plugin-persistedstate/nuxt',
    ],

    piniaPersistedstate: {
        cookieOptions: {
            sameSite: 'strict',
        },
        storage: 'cookies'
    },

    nitro: {
        preset: 'node-server',
        inlineDynamicImports: true
    },

    i18n: {
        strategy: 'no_prefix',
        vueI18n: './i18n.config.ts',
        detectBrowserLanguage: {
            useCookie: false,
        },
        locales: [
            {
                code: 'en-us',
                name: 'English (United States)'
            },
            {
                code: 'es',
                name: 'Español'
            }
        ]
    },

    app: {
        head: {
            link: [
                {
                    rel: 'stylesheet',
                    href: 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css'
                },
                {
                    rel: 'stylesheet',
                    href: '/css/style.css'
                }
            ],
            script: [
                {
                    src: 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js',
                    body: true
                },
                {
                    src: '/js/zexel-models.js',
                    body: true
                }
            ]
        }
    },

})
