 <template>
    <div class="home">
        <div class="header">
            <mt-header fixed title="首页"></mt-header>
        </div>
       <div>
           <mt-field placeholder="你想找什么工作" v-model="value    "></mt-field>
           <mt-button plain size="large" type="primary" @click="search">搜索</mt-button>
           <br>
       </div>
    <section class="swipe">
			<mt-swipe :auto="4000">
                <mt-swipe-item><img src="../assets/banner4.jpg" height="100%" width="100%" ></mt-swipe-item>
                <mt-swipe-item><img src="../assets/banner6.jpg" height="100%" width="100%"></mt-swipe-item>
                <mt-swipe-item><img src="../assets/banner8.jpg" height="100%" width="100%"></mt-swipe-item>
            </mt-swipe>
	</section>
    <p>{{data.job}}</p>
    <div class="xyk-strategy">
        <div class="title-box">
            <mt-cell title="职位推荐" value="" ></mt-cell>
        </div>
        <div>
            <div class="xyk-item" v-for="dat in data":dat="dat" @click="jump(dat._id)">
                <div class="left-icon-box">
                   <h3>{{dat.job}}</h3>
                </div>
    
                <div class="right-box">
                    <div class="time">{{dat.salary}}</div>  
                    <div class="time">{{dat.companyloc}}</div>
                    <div class="time">{{dat.expreq}}</div> 
                </div>
            </div>
        </div>
    </div>    

    <div>
        <mt-tabbar fixed v-model="selected">
        <mt-tab-item id="home" >
            <img slot="icon" src="../assets/home1.png" v-if="this.selected=='home'">
            <img slot="icon" src="../assets/home.png" v-else>
            首页
        </mt-tab-item>
        <mt-tab-item id="type">
            <img slot="icon" src="../assets/type1.png" v-if="this.selected=='type'">
            <img slot="icon" src="../assets/type.png" v-else>
            分类
        </mt-tab-item>
        <mt-tab-item id="search">
            <img slot="icon" src="../assets/工资（1）.png" v-if="this.selected=='search'">
            <img slot="icon" src="../assets/工资.png" v-else>
            薪资预测
        </mt-tab-item>
        <mt-tab-item id="search">
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
  name: 'home',
  data () {
    return{
      selected:"home",
      data:[],
    };
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
            }
        }
    },
    created(){
        this.gets()
    },
    methods:{
        gets:function(){
            var that=this;
            $.get("http://120.79.177.232:8000",function(response){
                that.data=response
                console.log(that.data)
                console.log(that.selected)
            })
        },
        search:function(){
            this.$router.push('/searchpage/'+this.value)
        },
        jump:function(id){
            var that=this
            that.$router.push('/job/'+id);
        }
    }
  
}

</script>
<style>
.header{
    height: 0.1rem;
    background-color: white
    
}
.swipe{
    width: 100%;
	height: 13rem;
}
.search{
    height: 3.2rem;
    width: 100%;
    background-color: aliceblue
}
.xyk-item{
    display: flex;
    border-bottom: 0.5px solid lightgrey;
}
 
.xyk-item .left-icon-box{
    flex: 0 0 100px;
    align:center
}
 
.xyk-item .left-icon-box img{
    width: 80px;
    height: 80px;
    margin-left: 16px;
    margin-top: 10px;
}
.xyk-item .right-box{
    flex: 1;
}
 
.xyk-item .right-box .name{
    margin-top: 10px;
    margin-left: 10px;
    margin-right: 20px;
    font-size: 14px;
    color: black;
 
    height: 40px;
    line-height: 20px;
    overflow: hidden;
    word-break: break-all;
}
 
.xyk-item .right-box .time{
    display: block;
    margin-top: 10px;
    margin-left: 10px;
    margin-bottom: 10px;
}
.xyk-strategy{
    margin-bottom: 50px
}
</style>
