<template>
  <nav class="wrapper">
    <Logo/>
    <div class="search">
      <Input placeholder="Search"/>
      <Button class="box btn-primary"><SearchIcon/></Button>
      <Button class="box btn-light"><FilterIcon/></Button>
    </div>
    <div class="menu">
      <HearthIcon/>
      <Button class="btn-primary">Join Us</Button>
      <p>or</p>
      <p class="btn">Login</p>
    </div>
  </nav>
</template>

<script>
import Input from "@/components/ui/Input.vue";
import Button from "@/components/ui/Button.vue";
import Logo from "@/assets/icons/Logo.vue";
import SearchIcon from "@/assets/icons/SearchIcon.vue";
import FilterIcon from "@/assets/icons/FilterIcon.vue";
import HearthIcon from "@/assets/icons/HearthIcon.vue";
export default {
  name: "Header",
  components: {
    Button,
    Input,
    Logo,
    SearchIcon,
    FilterIcon,
    HearthIcon,
  }
}
</script>

<style scoped>
nav {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  padding-top: 12px;
  padding-bottom: 12px;
}
.menu {
  display: flex;
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
</style>
