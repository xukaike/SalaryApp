// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import MintUI from 'mint-ui'
import 'mint-ui/lib/style.css'
import $ from 'jquery'
import axios from 'axios'
import VueAxios from 'vue-axios'
axios.defaults.headers['Accept'] = 'application/json, text/plain, */*';
axios.defaults.timeout = 2000;
axios.defaults.withCredentials = true;//允许携带cookies

Vue.use(VueAxios, axios)
Vue.config.productionTip = false
Vue.use(MintUI)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
})
