import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axsio from 'axios'

axsio.defaults.baseURL = 'unix:/tmp/gunicorn.sock' 

createApp(App).use(store).use(router, axsio).mount('#app')
