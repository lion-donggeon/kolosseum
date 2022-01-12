<template>
    <div>
        <Header></Header>
        <!-- v-bind:하위컴포넌트 속성명="상위 컴포넌트 전달할 데이터명"  -->
        <Content v-bind:propsdata="nftProjectList"></Content>
        <Footer></Footer>
    </div>
</template>

<script>
import axios from "axios";
import Header from "./components/Header.vue";
import Content from "./components/Content.vue";
import Footer from "./components/Footer.vue";

let url = "http://localhost:8000/dao/";  // 장고 drf 서버 주소

export default {
    data: () => {
      return {
        nftProjectList: []
      };
    },
    components: {
        Header,
        Content,
        Footer,
    },
    mounted() { // DOM 객체가 생성된 후 DRF server 에서 데이터를(nftProjectList) 가져와 저장
      axios({
        method: "GET",
        url: url 
      })
        .then(response => {
          this.nftProjectList = response.data;
        })
        .catch(response => {
          console.log("Failed", response);
        });
    },
    methods: {  // CRUD 로직 
      getNftProjectList: function() {},
      updateNftProjectList: function() {},
      deleteNftProjectList: function() {},
    },
};
</script>

<style></style>