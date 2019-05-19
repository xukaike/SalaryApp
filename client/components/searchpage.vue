

<template>


  <div class="hello">
<mt-header fixed v-bind:title="key">
  <router-link to="/" slot="left">
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
  </div>
</template>


<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      list: [],
        loading: false,
        key:this.$route.params.key,
        time:0,
        lsits:[],
        ids:[],
    }
  },
     methods: {
      loadMore() {
        this.loading = true;
        setTimeout(() => {
            var that=this
          let last = this.list[this.list.length - 1];
          $.post("http://120.79.177.232:8000/findbyword",{count:'20',turn:that.time,keyword:that.key},function(response){
                for (let i = 0; i < 20; i++) {
                    that.list.push(response[i]);
                }
                that.time++
                console.log(that.list)
                console.log(that.key)  
                console.log(that.time)
                console.log(that.id)
            })
          
          this.loading = false;
        }, 1000);
      },
      gets:function(){
            var that=this;
            $.post("http://120.79.177.232:8000/findbyword",{count:'20',turn:that.time,keyword:that.key},function(response){
                that.list=response
                console.log(that.list)
                console.log(that.key)  
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
