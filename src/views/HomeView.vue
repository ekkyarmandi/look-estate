<template>
  <Header />
  <div class="container flex justify-between items-end text-secondary-500 text-sm">
    <p>ShortBy</p>
    <p>Results</p>
  </div>
  <div class="container">
    <ul class="flex flex-wrap justify-between">
      <li v-for:="item in items"><ListingItem /></li>
    </ul>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "@/components/Header.vue";
import ListingItem from "@/components/ListingItem.vue";

export default {
  name: "HomeView",
  data() {
    return {
      items: [1, 2, 3, 4],
    };
  },
  components: {
    Header,
    ListingItem,
  },
};
</script>

<style scoped>
.container {
  padding: 12px 50px 0px 50px;
  max-width: 1440px;
}
</style>
