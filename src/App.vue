<template>
  <!-- <router-link to="/">Home</router-link> -->
  <Copyright />
  <Header />
  <router-view/>
</template>

<script>
import Header from "@/components/Header.vue";
import Copyright from "@/components/Copyright.vue";
export default {
  name: 'App',
  components: {
    Header,
    Copyright,
  }
}
</script>

<style src="./assets/global.css"></style>
<style>
* {
  margin: 0;
  padding: 0;
}
#app {
  font-family: 'Inter', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.wrapper{
  padding-left: 3.125rem;
  padding-right: 3.125rem;
  max-width: 1440px;
}
</style>
