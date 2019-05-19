import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import type from '@/components/type'
import search from '@/components/search'
import center from '@/components/center'
import joblist from '@/components/joblist'
import job from '@/components/job'
import login from '@/components/login'
import searchpage from '@/components/searchpage'
import changemsg from '@/components/changemsg'
import changepasswd from '@/components/changepasswd'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: home
    },
    {
      path: '/type',
      component: type
    },
    {
      path: '/search',
      component: search
    },
    {
      path: '/center/:data',
      component: center
    },
    {
      path: '/joblist/:id',
      component: joblist
    },
    {
      path: '/job/:ids',
      component: job
    },
    {
      path: '/login',
      component: login
    },
    {
      path: '/searchpage/:key',
      component: searchpage
    },
    {
      path: '/changemsg/:data',
      component: changemsg
    },
    {
      path:'/changepasswd/:data',
      component:changepasswd
    }
  ]
})
