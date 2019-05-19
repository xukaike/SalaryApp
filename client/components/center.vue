<template>
  <div >
    <mt-header fixed title="我的"></mt-header>


 <mt-cell align="left" title="账号：" v-bind:value="lists.logid">
     <img slot="icon" src="../assets/账号 (1).png" width="36" height="36">
 </mt-cell>
<mt-cell align="left" ></mt-cell>
<mt-cell align="left" title="姓名" v-bind:value="lists.username">
    <img slot="icon" src="../assets/姓名.png" width="36" height="36">
</mt-cell>
<mt-cell align="left" title="邮箱：" v-bind:value="lists.mail">
    <img slot="icon" src="../assets/邮箱.png" width="36" height="36">
</mt-cell>
<mt-cell align="left" title="年龄：" v-bind:value="lists.age">
    <img slot="icon" src="../assets/年龄.png" width="36" height="36">
</mt-cell>
<mt-cell align="left" title="学历：" v-bind:value="lists.education">
    <img slot="icon" src="../assets/学历.png" width="36" height="36">
</mt-cell>
<mt-cell align="left" title="户籍：" v-bind:value="lists.residence">
    <img slot="icon" src="../assets/地方网址.png" width="36" height="36">
</mt-cell>
<mt-cell align="left" title="手机：" v-bind:value="lists.phone">
    <img slot="icon" src="../assets/手机.png" width="36" height="36">
</mt-cell>
<br><br>
<mt-button type="primary" size="large" plain @click="changemsg">修改信息</mt-button><br>
<mt-button type="danger" size="large" plain @click="changepasswd">修改密码</mt-button><br>
<mt-button type="danger" size="large" @click="unlogin">退出登录</mt-button><br><br><br>
 <div >
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
        <mt-tab-item id="center">
            <img slot="icon" src="../assets/center1.png" v-if="this.selected=='center'">
            <img slot="icon" src="../assets/center.png" v-else>
            我的
        </mt-tab-item>
        </mt-tabbar>
    </div>
  </div>
</template>
<style >


a {
  color: #26a2ff;
}
.filed{
  background-color: #26a2ff
}
</style>



<script>
export default {
  name: 'type',
  data () {
    return{
      selected:"center",
      list:this.$route.params.data,
      lists:[],
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
    methods:{
        unlogin:function(){
            window.localStorage.login='false'
            this.$router.push('/login')
        },
        getdata:function(){
            $.post("http://120.79.177.232:8000/queryuser",{logid:that.username,passwd:that.password},function(response){
                
            })
        },
        changemsg:function(){
            this.$router.push('/changemsg/'+this.list)
        },
        changepasswd:function(){
            this.$router.push('/changepasswd/'+this.list)
        }
    },
    mounted(){
        this.lists=JSON.parse(this.list)
        console.log(this.lists)
    },

  
}

</script>