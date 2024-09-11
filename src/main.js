import { createApp } from "vue";
import { createPinia } from "pinia";
import { createHead } from '@unhead/vue'
import App from "./App.vue";
import router from "./router";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";

const head = createHead()
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

createApp(App).use(router).use(pinia).use(head).mount("#app");
