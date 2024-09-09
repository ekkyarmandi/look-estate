<template>
  <nav class="wrapper">
    <a href="/">
      <Logo />
    </a>
    <div class="search">
      <Input placeholder="Search" />
      <Button class="box btn-primary"><SearchIcon /></Button>
      <Button class="box btn-light"><FilterIcon /></Button>
    </div>
    <div class="menu">
      <HearthIcon />
      <Button class="btn-primary p-lg">Join Us</Button>
      <p>or</p>
      <p class="btn">Login</p>
    </div>
    <div class="burger-menu">
      <HearthIcon />
      <Button class="box btn-light"><FilterIcon /></Button>
      <Button class="box btn-primary"><SearchIcon /></Button>
      <Button class="box btn-primary"><BurgerMenuIcon /></Button>
    </div>
  </nav>
</template>

<script setup>
import Input from "@/components/ui/Input.vue";
import Button from "@/components/ui/Button.vue";
import Logo from "@/assets/icons/Logo.vue";
import SearchIcon from "@/assets/icons/SearchIcon.vue";
import BurgerMenuIcon from "@/assets/icons/BurgerMenuIcon.vue";
import FilterIcon from "@/assets/icons/FilterIcon.vue";
import HearthIcon from "@/assets/icons/HearthIcon.vue";
</script>

<style scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  padding-top: 12px;
  padding-bottom: 12px;
}
.p-lg {
  padding: 0 20px;
}
.menu,
.burger-menu {
  display: none;
  gap: 12px;
  justify-content: flex-end;
  align-items: center;
}
.search {
  display: flex;
  gap: 12px;
}
.btn {
  cursor: pointer;
  color: var(--primary-500);
  text-decoration: underline;
}
@media only screen and (max-width: 600px) {
  .burger-menu {
    display: flex;
  }
  .search {
    display: none;
  }
}
@media only screen and (min-width: 600px) {
  .menu {
    display: flex;
  }
  .menu > p {
    display: none;
  }
  nav .search {
    flex-grow: 1;
  }
}
@media only screen and (min-width: 1200px) {
  nav {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
  }
}
</style>
