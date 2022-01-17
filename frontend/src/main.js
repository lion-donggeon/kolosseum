import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axsio from 'axios'

//로컬
//axsio.defaults.baseURL = 'http://localhost:8000/' 

//운영
axios.defaults.baseURL = 'http://15.165.73.177/' 

createApp(App).use(store).use(router, axsio).mount('#app')
