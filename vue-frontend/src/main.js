import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import HomePage from "@/components/HomePage.vue";

const app = createApp(HomePage)

app.use(createPinia())

app.mount('#app')
