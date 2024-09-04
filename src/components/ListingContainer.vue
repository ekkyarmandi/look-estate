<template>
  <div class="wrapper listing-container">
    <ul>
      <li v-for:="item in items">
        <ListingItem />
      </li>
    </ul>
    <l-dot-pulse size="43" speed="1.3" color="#42b983"></l-dot-pulse>
  </div>
</template>

<script setup>
import { ref } from "vue";
import ListingItem from "@/components/ListingItem.vue";
const items = ref([1, 2, 3, 4, 5, 6, 7, 8]);
</script>

<style scoped>
ul {
  display: grid;
  grid-template-columns: repeat(3, min(427px));
  justify-content: space-between;
  row-gap: 30px;
  width: 100%;
  list-style-type: none;
}
.listing-container {
  margin-bottom: 40px;
}
</style>
