<script >
// 声明式渲染：vue2
export default{
  data(){
    return {
      // 声明变量
      num : 0,
      uname : "张三",
      msg : "<h2>标题</h2>",
      id : "d1",
      attrNum:'id',
      mouseEvent:'click',
      isActive:true,
      user:{
        name:"李四",
        age:18,
        sex:"男"
      },
      class_obj:{
        active:true,
        c:true,
      }
    };
  },
  methods :{
    // 给vue定义方法
    changeUname: function(){
      // this 指的是当前的vue实例
      this.uname='李四'
    },
    reverseMessage:function(){
      // console.log("函数")
      this.uname.split('').reverse().join('')
    }
  },
  computed:{
    // reverseMsg:function(){
    //   console.log("计算属性")
    //   return this.uname.split('').reverse().join('')
    // } 
    reverseMsg:{
      get:function(){
        return this.uname.split('').reverse().join('');
      },
      set:function(newValue){
        // console.log(newValue);
        this.uname=newValue;
      }
    },

  },
  // 监听
  watch:{
    // 变量
    uname:{
      immediate: true,// 初始化的时候就调用函数
      // 监听每当数据变化时，就会调用这个函数
      handler:function(newValue, oldValue){
        console.log(newValue);
        console.log(oldValue);
        // 执行复杂操作或逻辑代码
        if(newValue.length < 5 || newValue.length > 10 ){
          console.log("输入新数据不能小于5或者大于10");
        }
      },
    },
    // 不能监听对象的属性变化，需要深度监听
    // user:{
    //   handler:function(newValue){
    //     console.log("============",newValue);
    //   },
    //   deep:true,// 开启深度监听，会一层一层地向下监听对象的每个属性
    // },
    // 监听对象的某一个属性
    "user.name":{
      handler:function(newValue){
        console.log(newValue);
      },
      deep:true,
    }
  }
}
</script>

<template>
 <div>
    <!-- <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Hello Vue 3 + Vite" />  -->
    <!-- <p>{{ num }}</p>  -->
    <!-- <p>{{ uname }}</p>  -->
    <!-- <p v-once> {{ uname }} </p> -->
    <!-- <button @click="changeUname"> 改变名字 </button> -->
    <!-- <p v-html="msg"></p> -->
    <!-- <p v-bind:id="id">v-bind绑定</p> -->
    <!-- <p :id="id"> 省略v-bind </p> -->
    <!-- html属性内可以直接使用js语法 -->
    <!-- <button @click="id='d2'">改变颜色</button> -->
    <!-- 变量值反转 --> 
    <p>{{ uname.split('').reverse().join('') }}</p> -->
    <!-- v-on : 语法糖 -->
    <button v-on:click='changeUname'>v-on</button>
    <!-- 动态参数 ： 动态属性-->
    <button v-bind:[attrNum]='id'>动态属性</button>
    <button @click="attrNum='class'">动态属性</button>
    <!-- 动态事件 -->
    <button @[mouseEvent]="attrNum='class'">改变事件</button>
    <button @click="mouseEvent='mouseover'">改变事件</button>
    <!-- 计算属性及与js和函数的区别 -->
    <!-- js属性 -->
    <p>{{ uname.split('').reverse().join('') }}</p>
    <p>{{ uname.split('').reverse().join('') }}</p>
    <p>{{ uname.split('').reverse().join('') }}</p>
    <!-- 计算属性 -->
    <p>{{ reverseMsg  }}</p>
    <p>{{ reverseMsg  }}</p>
    <p>{{ reverseMsg  }}</p>
    <!-- 函数 -->
    <p>{{ reverseMessage() }}</p>
    <p>{{ reverseMessage() }}</p>
    <p>{{ reverseMessage() }}</p>
    
    <!-- 计算属性的getter和setter -->
    <button @click="reverseMsg='历史'"> 改变reverseMsg </button>
    <input type="text" v-model="uname">
    <button @click="user.name='王五'">{{ user.name }}</button>

    
    <!-- Class 和 Style的关系 -->
    <!-- 第一种放置字符串 -->
    <p class='active'>Hello</p>
    <!-- 第二种：放置对象 -->
    <p :class="{active:isActive}">Hi</p>
        <!--多个类对象绑定 -->
    <p :class="class_obj">World</p>
    <button @click="isActive=!isActive">改变Active</button>



 </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#d1{
  color:red;
}
.d1{
  font-size: 50px;
}
#d2{
  color: blue;
}
.active{
  font-size: 50px;
  color: blue;
}
.c{
  background:pink;
}
</style>
