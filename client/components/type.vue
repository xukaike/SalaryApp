<template>
    <div>
        


<mt-header fixed title="类别"></mt-header>

<template>
  <div align="left">
        <mt-cell 
          title="Python" 
          label="" 
          is-link
          to="/joblist/Python">
          <img slot="icon" src="../assets/python.png" width="36" height="36">
        </mt-cell>
        <mt-cell class="body"
          title="Java" 
          label=""  
          to="/joblist/Java" 
          is-link >
          <img align="center" slot="icon" src="../assets/java(1).png" width="36" height="36">
        </mt-cell>
     


        <mt-cell class="body"
          title="Linux" 
          label=""  
          to="/joblist/Linux" 
          is-link >
          <img slot="icon" src="../assets/linux.png" width="36" height="36">
        </mt-cell>
        
        <mt-cell class="body"
          title="Web" 
          label=""  
          to="/joblist/Web"     
          is-link >
          <img slot="icon" src="../assets/web.png" width="36" height="36">
        </mt-cell>
        

        <mt-cell class="body"
          title="人工智能" 
          label=""  
          to="/joblist/人工智能" 
          is-link >
          <img slot="icon" src="../assets/人工智能.png" width="36" height="36">
        </mt-cell>
        
        <mt-cell class="body"
          title="前端" 
          label=""  
          to="/joblist/前端" 
          is-link >
          <img slot="icon" src="../assets/前端.png" width="36" height="36">
        </mt-cell>
       
        <mt-cell class="body"
          title="大数据" 
          label=""  
          to="/joblist/大数据" 
          is-link >
          <img slot="icon" src="../assets/大数据.png" width="36" height="36">
        </mt-cell>
       
        <mt-cell class="body"
          title="嵌入式" 
          label=""  
          to="/joblist/嵌入式" 
          is-link >
          <img slot="icon" src="../assets/系统.png" width="36" height="36">
        </mt-cell>
       
        <mt-cell class="body"
          title="数据分析" 
          label=""  
          to="/joblist/数据分析" 
          is-link >
          <img slot="icon" src="../assets/数据分析.png" width="36" height="36">
        </mt-cell>
        
        <mt-cell class="body"
          title="软件测试" 
          label=""  
          to="/joblist/软件测试" 
          is-link >
          <img slot="icon" src="../assets/软件.png" width="36" height="36">
        </mt-cell>
    
    </div>
</template>
        <div>
        <mt-tabbar v-model="selected" fixed>
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
  name: 'type',
  data () {
    return{
      selected:"type"
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
    }
  
}

</script>
<style>
    .cell{
        height: 100px;
    }
    .body{
        margin-top: 20px
    }
</style>
