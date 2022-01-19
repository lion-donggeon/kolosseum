import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

//로컬
axios.defaults.baseURL = 'http://localhost:8000/' 

//운영
//axios.defaults.baseURL = 'http://kolosseum.land/' 

createApp(App).use(store).use(router, axios).mount('#app')
