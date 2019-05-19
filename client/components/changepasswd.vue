<template>
  <div >
    <mt-header fixed title="修改">
    </mt-header>


 <mt-field  align="left" label="原密码：" v-model:value="passwd">
 </mt-field >
<mt-cell align="left" ></mt-cell>
<mt-field  align="left" label="新密码：" v-model:value="newpasswd">
</mt-field >
<mt-field  align="left" label="确认新密码：" v-model:value="checknewpasswd">
</mt-field >

<br><br>
<mt-button type="primary" size="large" plain @click="finish">确定</mt-button><br>
 
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
      lists:[],
      passwd:'',
      newpasswd:'',
      checknewpasswd:''
    };
  },
    methods:{
        finish:function(){
            console.log(this.passwd)
            console.log(this.newpasswd)
            console.log(this.checknewpasswd)
            console.log(this.lists._id)
            var that=this
            $.post("http://120.79.177.232:8000/editpsw",{original:that.passwd,passwd:that.newpasswd,confirm:that.checknewpasswd,id:that.lists._id},function(response){
                if(response=='new password error'){
                    alert('密码不一致')
                    console.log(response)
                }
                else if(response=='original password error'){
                    alert('原密码错误')
                    console.log(response)
                }
                else{
                    that.lists.passwd=that.newpasswd
                    that.list=JSON.stringify(that.lists)
                    that.$router.push('/center/'+that.list)
                    console.log(response)
                }
            })
        }
    },
    mounted(){
        this.lists=JSON.parse(this.list)
        console.log(this.lists)
    },

  
}

</script>