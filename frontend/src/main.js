import Antd from "ant-design-vue";
import { createApp } from "vue";
import { createPinia } from "pinia";

import Popper from "vue3-popper";
import VueClickAway from "vue3-click-away";

import App from "./App.vue";
import router from "./router";

// Style
import "@/assets/tailwind.css";
import "ant-design-vue/dist/antd.css";
import "@/assets/variables.less";
import "@/assets/main.less";

const app = createApp(App);

// Components
app.component("Popper", Popper);

app.use(createPinia());
app.use(router);
app.use(Antd);
app.use(VueClickAway)

app.mount("#app");
