

<template>


  <div class="hello">
<mt-header fixed v-bind:title="id">
  <router-link to="/type" slot="left">
    <mt-button icon="back">返回</mt-button>
  </router-link>
</mt-header>
      <div class="bar">
      <ul align='left'class="page-infinite-list" v-infinite-scroll="loadMore" infinite-scroll-disabled="loading" infinite-scroll-distance="1">
        <div @click="jump(item._id)" v-for="item in list":item="item">
            <mt-cell
            class="page-infinite-listitem"
            v-bind:title="item.job" 
            v-bind:label="item.companyloc" 
             ></mt-cell> 
        </div>
          <p v-show="loading" align='center' class="page-infinite-loading">
              
        <mt-spinner type="triple-bounce" color="#26a2ff"></mt-spinner>
      
      </p>
      </ul>
      </div>
      <div>
        <mt-tabbar fixed v-model="selected">
        <mt-tab-item id="home" >
            <img slot="icon" src="../assets/home1.png" v-if="this.selected=='home'">
            <img slot="icon" src="../assets/home.png" v-else>
            首页
        </mt-tab-item>
        <mt-tab-item id="type">
            <img slot="icon" src="../assets/type1.png" v-if="this.selected=='type'||'joblist'">
            <img slot="icon" src="../assets/type.png" v-else>
            分类
        </mt-tab-item>
        <mt-tab-item id="search">
            <img slot="icon" src="../assets/工资（1）.png" v-if="this.selected=='search'">
            <img slot="icon" src="../assets/工资.png" v-else>
            薪资预测
        </mt-tab-item>
        <mt-tab-item id="center">
            <img slot="icon" src="../assets/center1.png" v-if="this.selected=='center'">
            <img slot="icon" src="../assets/center.png" v-else>
            我的
        </mt-tab-item>
        </mt-tabbar>
    </div>



  </div>
</template>


<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      list: [],
        loading: false,
        selected:"joblist", 
        id:this.$route.params.id,
        time:0,
        lsits:[],
        ids:[],
    }
  },
  watch: {
        selected: function (selected) {
            switch(selected){
                case 'home':
                    this.$router.push('/');
                break;
                case 'type':
                    this.$router.push('/type');
                break;
                case 'search':
                    this.$router.push('/search');
                break;
                case 'login':
                    this.$router.push('/login');
                break;
                case 'joblist':
                    this.$router.push('/joblist');
                break;
            }
        },
    },
     methods: {
      loadMore() {
        this.loading = true;
        setTimeout(() => {
            var that=this
          let last = this.list[this.list.length - 1];

          $.post("http://120.79.177.232:8000/search",{count:'20',turn:that.time,jobkeyword:that.id},function(response){
                for (let i = 0; i < 20; i++) {
                    that.list.push(response[i]);
                }
                that.time++
                console.log(that.list)
                console.log(that.selected)  
                console.log(that.time)
                console.log(that.id)
            })
          
          this.loading = false;
        }, 1000);
      },
      gets:function(){
            var that=this;

            $.post("http://120.79.177.232:8000/search",{count:'20',turn:that.time,jobkeyword:that.id},function(response){
                that.list=response
                console.log(that.list)
                console.log(that.selected)  
                console.log(that.time)
                console.log(that.id)
            })
        },
        jump:function(id){
            var that=this
            that.$router.push('/job/'+id);
        }
    },
    mounted(){
        this.gets()
    }
}
</script>
<style>
.bar{
      margin-bottom: 60px
  }
</style>
