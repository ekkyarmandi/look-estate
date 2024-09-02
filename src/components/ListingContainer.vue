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

<script>
import ListingItem from "@/components/ListingItem.vue";

export default {
  name: "ListingContainer",
  components: {
    ListingItem,
  },
  data() {
    return {
      items: [1, 2, 3, 4, 5, 6, 7, 8],
    };
  },
};
</script>

<style scoped>
ul {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px 30px;
  list-style-type: none;
}
ul li {
  display: flex;
  justify-content: center;
}
.listing-container {
  margin-bottom: 40px;
}
</style>
