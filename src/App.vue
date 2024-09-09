<template>
  <Copyright />
  <div class="nav-border"><Header/></div>
  <router-view />
  <div class="footer-bg"><Footer/></div>
</template>

<script setup>
import Header from "@/components/Header.vue";
import Copyright from "@/components/Copyright.vue";
import Footer from "@/components/Footer.vue";
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

.nav-border {
  border-bottom: 1px solid #ccc;
}

.footer-bg {
  background-color: var(--secondary-500);
}

.wrapper {
  max-width: 1340px;
  margin: auto;
  height: fit-content;
}
@media only screen and (max-width: 600px) {
  .wrapper {
    padding-left: 18px;
    padding-right: 18px;
  }
}
@media only screen and (min-width: 600px) {
  .wrapper {
    padding-left: 18px;
    padding-right: 18px;
  }
}
@media only screen and (min-width: 768px) {
  .wrapper {
    padding-left: 24px;
    padding-right: 24px;
  }
}
@media only screen and (min-width: 992px) {
  .wrapper {
    padding-left: 30px;
    padding-right: 30px;
  }
}
@media only screen and (min-width: 1200px) {
  .wrapper {
    padding-left: 50px;
    padding-right: 50px;
  }
}
</style>
