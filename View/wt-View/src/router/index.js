import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import CustomCli from '@/components/CustomCli'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'CustomCli',
      component: CustomCli
    },
	 {
      path: '/Hello',
      name: 'Hello',
      component: Hello
    }
  ]
})
