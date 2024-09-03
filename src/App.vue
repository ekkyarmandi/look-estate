<template>
  <!-- <router-link to="/">Home</router-link> -->
  <Copyright />
  <div class="nav-border"><Header /></div>
  <router-view />
  <div class="footer-bg"><Footer /></div>
</template>

<script>
import Header from "@/components/Header.vue";
import Copyright from "@/components/Copyright.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "App",
  components: {
    Header,
    Copyright,
    Footer,
  },
};
</script>

<style src="./assets/global.css"></style>
<style>
* {
  margin: 0;
  padding: 0;
}
#app {
  font-family: "Inter", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.wrapper {
  padding-left: 3.125rem;
  padding-right: 3.125rem;
  max-width: 1440px;
  margin: auto;
}
.nav-border {
  border: 1px solid #ccc;
}
.footer-bg {
  background-color: var(--secondary-500);
}
</style>
