<template>
  <div >
    <mt-header fixed title="修改">
    </mt-header>


<mt-cell align="left" ></mt-cell>
<mt-field  align="left" label="姓名" v-model:value="lists.username">
    <img slot="icon" src="../assets/姓名.png" width="36" height="36">
</mt-field >
<mt-field  align="left" label="邮箱：" v-model:value="lists.mail">
    <img slot="icon" src="../assets/邮箱.png" width="36" height="36">
</mt-field >
<mt-field  align="left" label="年龄：" v-model:value="lists.age">
    <img slot="icon" src="../assets/年龄.png" width="36" height="36">
</mt-field >
<mt-field  align="left" label="学历：" v-model:value="lists.education">
    <img slot="icon" src="../assets/学历.png" width="36" height="36">
</mt-field >
<mt-field  align="left" label="户籍：" v-model:value="lists.residence">
    <img slot="icon" src="../assets/地方网址.png" width="36" height="36">
</mt-field >
<mt-field  align="left" label="手机：" v-model:value="lists.phone">
    <img slot="icon" src="../assets/手机.png" width="36" height="36">
</mt-field >
<br><br>
<mt-button type="primary" size="large" plain @click="finish">完成</mt-button><br>
 
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
      list:this.$route.params.data,
      lists:[]
    };
  },
    methods:{
        finish:function(){
            this.list=JSON.stringify(this.lists)
            this.$router.push('/center/'+this.list)
            console.log(this.list)
        }
    },
    mounted(){
        this.lists=JSON.parse(this.list)
        console.log(this.lists)
    },

  
}

</script>