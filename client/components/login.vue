<template>
    <div>
        <mt-header fixed title="登录"></mt-header>
        </br></br></br></br></br></br>
        <mt-field label="用户名" placeholder="请输入用户名" v-model="username"></mt-field></br>
        <mt-field label="密码" placeholder="请输入密码" type="password" v-model="password"></mt-field></br></br></br></br></br>
        <mt-button size="large" type="primary" @click="login">登录</mt-button>
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
        <mt-tab-item id="login">
            <img slot="icon" src="../assets/center1.png" v-if="this.selected=='login'">
            <img slot="icon" src="../assets/center.png" v-else>
            我的
        </mt-tab-item>
        </mt-tabbar>
    </div>
</template>
<script>
export default {
    data () {
    return{
      username:'',
      password:'',
      data:[],
      selected:'login'
    };
  },
  
  methods:{
      login:function(){
          var that=this
          $.post("http://120.79.177.232:8000/queryuser",{logid:that.username,passwd:that.password},function(response){
                if(response=='error'){
                    alert('登录失败！')
                    
                }
                else{
                    that.data=JSON.stringify(response)
                    window.localStorage.data=that.data
                    that.$router.push('/center/'+that.data);
                    window.localStorage.login='ture'
                    console.log(window.localStorage.login)
                }
            })
      },
      checklogin:function(){
          if(window.localStorage.login=='ture'){
            this.$router.push('/center/'+window.localStorage.data)
          }
          else{
              this.$router.push('/login')
          }
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
            }
        }
    },
  mounted(){
    this.checklogin()
}
}
</script>
