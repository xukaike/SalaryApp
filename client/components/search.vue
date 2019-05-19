<template>
    <div>



<template>
  <div class="hello" align="left" style="margin-bottom:100px">
      <mt-header fixed title="薪资预测"></mt-header>
      <mt-radio 
        title="公司类型"
        v-model="companytype"
        :options="['创业公司', '非营利组织', '国企','合资','民营公司','上市公司','事业单位','外资(非欧美)','外资(欧美)']">
      </mt-radio>
      <mt-radio 
        title="公司规模"
        v-model="companysize"
        :options="['10000人以上', '5000-10000人', '1000-5000人','500-1000人','150-500人','50-150人','少于50人',]">
      </mt-radio>
      <mt-radio 
        title="工作经验"
        v-model="expreq"
        :options="['无工作经验', '1年经验', '2年经验','3-4年经验','5-7年经验','8-9年经验','10年以上经验',]">
      </mt-radio>
      <mt-radio 
        title="学历"
        v-model="education"
        :options="['硕士', '本科', '大专','无要求']">
      </mt-radio>
      <mt-checklist

      title="是否掌握以下技能"

      v-model="skills"

      :options="options">

    </mt-checklist>
    <mt-button size="large" type="primary" @click="summit">提交</mt-button>

  </div>
</template>

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
import { Indicator } from 'mint-ui';
import { Toast } from 'mint-ui';
export default {
  name: 'search',
  data () {
    return{
      selected:"search",
      value:'',
      list:[],
      companytype:'',
      companysize:'',
      expreq:'',
      skills:[],
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
        },
    },
    created(){
      this.options=['Hive', 'Hadoop', 'Python','Sql','Spark','Sas','Tableau','Spss','PPT','Excel'];
    },
    methods:{
      
      summit:function(){
        Indicator.open({
        text: '加载中...',
        spinnerType: 'double-bounce'
      });
      setTimeout(() => Indicator.close(), 3000);
      }
    }
  
}

</script>
