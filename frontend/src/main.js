import { createApp } from 'vue'
import App from '@/App'
import router from '@/routers/index'

const app = createApp(App)

app.use(router).mount('#app')
