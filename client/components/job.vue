




<template>

    
  <div class="hello">
    <mt-header fixed title="详情">
  <router-link to="/" slot="left">
    <mt-button icon="back" @click="back">返回</mt-button>
  </router-link>
</mt-header>
    <div align='left'>
      <mt-cell 
        v-bind:title="data.job" 
        v-bind:label="data.companyloc">
        <span style="color: red" >{{data.salary}}</span>
      </mt-cell>       
    </div><br><br>
    <div align='left'>       
      <article>
        <mt-cell class="body"
          title="地址" 
          label="" >
          <img slot="icon" src="../assets/地址 (1).png" width="24" height="24">
        </mt-cell>
        <hr/>
        <p>{{data.workplace}}</p>		
      </article>
    </div>
    <div align='left'>       
      <article>
        <mt-cell class="body"
          title="公司类型" 
          label="" >
          <img slot="icon" src="../assets/公司类型 (1).png" width="24" height="24">
        </mt-cell>
        <hr/>
        <p>{{data.companyfield}}</p>		
      </article>
    </div>
    <div align='left'>       
      <article>
        <mt-cell class="body"
          title="经验要求" 
          label="" >
          <img slot="icon" src="../assets/经验 (2).png" width="24" height="24">
        </mt-cell>
        <hr/>
        <p>{{data.expreq}}</p>		
      </article>
    </div>
    <div align='left'>       
      <article>
        <mt-cell class="body"
          title="学历" 
          label="" >
          <img slot="icon" src="../assets/博士.png" width="24" height="24">
        </mt-cell>
        <hr/>
        <p>{{data.education}}</p>		
      </article>
    </div>
    <div align='left'>       
      <article>
        <mt-cell class="body"
          title="职位描述" 
          label="" >
          <img slot="icon" src="../assets/职位岗位.png" width="24" height="24">
        </mt-cell>
        <hr/>
        <p>{{data.jobdescription}}</p>		
      </article>
    </div>
    

    
    <div align='left' style="margin-bottom:50px">
      <table style="font-size:8px">
        <br/>
		<h5>警示：以招聘为名收取培训费用、提供培训贷款，或在录用过程中需支付体检、服装、押
      金等费用的，都属违法行为。一经发现，请立即举报，并向当地公安机关报案。</h5>
      </table>
	</div>
  <div>
        <mt-tabbar fixed v-model="selected">
        <mt-tab-item id="home" >
            <img slot="icon" src="../assets/home1.png" v-if="this.selected=='home'">
            <img slot="icon" src="../assets/home.png" v-else>
            首页
        </mt-tab-item>
        <mt-tab-item id="type">
            <img slot="icon" src="../assets/type1.png" v-if="this.selected=='type'||'joblist'||'job'">
            <img slot="icon" src="../assets/type.png" v-else>
            分类
        </mt-tab-item>
        <mt-tab-item id="search">
            <img slot="icon" src="../assets/工资（1）.png" v-if="this.selected=='search'">
            <img slot="icon" src="../assets/工资.png" v-else>
            薪资预测
        </mt-tab-item>
        <mt-tab-item id="login">
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
      selected:"job",
      id:this.$route.params.ids,
      data:[],
      detail:''
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
                case 'job':
                    this.$router.push('/job');
                break;
            }
        }
    },
    methods:{
      back(){
        this.$router.back(-1)
      },
      getdata:function(){
          var that=this;
            $.post("http://120.79.177.232:8000/detail",{id:that.id},function(response){
                that.data=response
                console.log(that.data)
                console.log(that.selected)
                console.log(that.data.jobdescription)
            })
      }
    },
    
    created(){
        this.getdata()
    }
}
</script>
