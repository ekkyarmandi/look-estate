<template>
  <div class="wrapper listing-container">
    <ResultFound :total="resultFound" />
    <ul ref="listingContainer">
      <li v-if:="items.length > 0" v-for:="item in items">
        <ListingItem :data="item" :key="item.id" />
      </li>
      <ListingSkeleton v-else: />
    </ul>
    <div class="loading">
      <div v-if:="isLoading"><LoadingSpinner /></div>
      <Button v-else: class="btn-primary w-lg" @click="loadMore">Load More</Button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useRoute } from "vue-router";

import LoadingSpinner from "@/components/LoadingSpinner.vue";
import ListingSkeleton from "@/components/ListingSkeleton.vue";
import ListingItem from "@/components/ListingItem.vue";
import ResultFound from "@/components/ResultFound.vue";
import Button from "@/components/ui/Button.vue";

const router = useRoute();

const items = ref([]);
const isLoading = ref(true);
const prefix = ref("");
const total = ref(0);
const page = ref(1);
const listingContainer = ref(null);

onMounted(() => {
  prefix.value = process.env.VUE_APP_API_URL;
});

onMounted(() => {
  var url = prefix.value + "/properties";
  if (router.query.q) {
    url = prefix.value + "/properties?q=" + router.query.q;
  }
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      items.value.push(...data.results);
      isLoading.value = false;
      total.value = data.total;
    });
});

const resultFound = computed(() => {
  return total.value.toLocaleString();
});

const loadMore = () => {
  isLoading.value = true;
  page.value += 1;
  const url = prefix.value + "/properties?page=" + page.value;
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      items.value.push(...data.results);
      isLoading.value = false;
    })
    .catch((err) => {
      console.log(err);
      isLoading.value = false;
      // TODO: show notification to user
    });
};
</script>

<style scoped>
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}
.listing-container {
  height: 100%;
}
ul {
  justify-content: space-between;
  width: 100%;
  list-style-type: none;
}
.w-lg {
  padding: 0px 20px;
}
@media only screen and (max-width: 600px) {
  ul {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
}
@media only screen and (min-width: 600px) {
  ul {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
  }
  ul li {
    width: 48%;
  }
}
@media only screen and (min-width: 992px) {
  ul {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
  }
  ul li {
    width: 32%;
  }
}
</style>
