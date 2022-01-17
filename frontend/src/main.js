import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axsio from 'axios'

axsio.defaults.baseURL = 'http://15.165.73.177' 

createApp(App).use(store).use(router, axsio).mount('#app')
