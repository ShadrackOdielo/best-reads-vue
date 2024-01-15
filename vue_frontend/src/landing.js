import {createApp} from 'vue'
import {createPinia} from 'pinia'
import DjangoUtilsPlugin from 'vue-plugin-django-utils'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import {convertDatasetToProps} from 'vue-plugin-django-utils'

import LandingPage from "@/components/LandingPage.vue";
import ContactsSection from "@/components/BookItem.vue";
import AboutMeSection from "@/components/BookList.vue";
import DescriptionSection from "@/components/DescriptionSection.vue";
import HomeSection from "@/components/HomeSection.vue";

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
const app = createApp(LandingPage)
app.use(pinia)
app.use(DjangoUtilsPlugin, {
    convertDatasetToProps: convertDatasetToProps,
})
app.component('ContactsSection', ContactsSection)
app.component('AboutMeSection', AboutMeSection)
app.component('DescriptionSection', DescriptionSection)
app.component('HomeSection', HomeSection)
app.mount('#app')
