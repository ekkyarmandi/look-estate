<template>
  <div class="wrapper listing-container">
    <div v-if:="bookmarked.length == 0" class="">
      <p class="empty-text">No Bookmark</p>
    </div>
    <ul v-else: ref="listingContainer">
      <li v-for:="item in bookmarked">
        <ListingItem :data="item" :key="item.id" />
      </li>
    </ul>
  </div>
</template>

<script setup>
import ListingItem from "@/components/ListingItem.vue";
import { useBookmarkStore } from "@/store/bookmark";
import { storeToRefs } from "pinia";

const bookmarkStore = useBookmarkStore();
const { bookmarked } = storeToRefs(bookmarkStore);
</script>

<style scoped>
.listing-container {
  min-height: 600px;
  padding: 20px 50px;
}
ul {
  justify-content: space-between;
  width: 100%;
  list-style-type: none;
}
.w-lg {
  padding: 0px 20px;
}
.empty-text {
  text-align: center;
  font-size: 24px;
  color: var(--secondary-500);
  margin-top: 20px;
}
@media only screen and (max-width: 600px) {
  ul {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
}
@media only screen and (min-width: 600px) {
  .listing-container {
    padding: 20px 18px;
  }
  ul {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
  }
  ul li {
    width: 48%;
  }
}
@media only screen and (min-width: 785px) {
  .listing-container {
    padding: 20px 24px;
  }
}
@media only screen and (min-width: 992px) {
  .listing-container {
    padding: 20px 30px;
  }
  ul {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
  }
  ul li {
    width: 32%;
  }
}
@media only screen and (min-width: 1200px) {
  .listing-container {
    padding: 20px 50px;
  }
}
</style>
