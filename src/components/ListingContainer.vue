<template>
  <div class="wrapper listing-container">
    <ResultFound v-if="items.length > 0" :total="resultFound" />

    <div v-if="isLoading" class="skeleton-grid">
      <div v-for="i in 6" :key="i" class="skeleton-item">
        <ListingSkeleton />
      </div>
    </div>

    <template v-else>
      <ul ref="listingContainer" v-if="items.length > 0">
        <li v-for="item in items" :key="item.id">
          <ListingItem :data="item" />
        </li>
      </ul>
      <EmptyState v-else />
    </template>

    <div class="loading" v-if="items.length > 0">
      <div v-if="isLoading"><LoadingSpinner /></div>
      <Button
        v-else-if="total > items.length"
        class="btn-primary w-lg"
        @click="loadMore"
        >Load More</Button
      >
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue";
import { useRoute } from "vue-router";

import LoadingSpinner from "@/components/LoadingSpinner.vue";
import ListingSkeleton from "@/components/ListingSkeleton.vue";
import ListingItem from "@/components/ListingItem.vue";
import ResultFound from "@/components/ResultFound.vue";
import EmptyState from "@/components/EmptyState.vue";
import Button from "@/components/ui/Button.vue";
import { useHead } from "@unhead/vue";

const route = useRoute();

useHead({
  title: "Home Page | Look Estate",
  meta: [
    {
      name: "description",
      content: "Property listing websites",
    },
  ],
});

const items = ref([]);
const isLoading = ref(true);
const total = ref(0);
const page = ref(1);
const listingContainer = ref(null);

const prefix = process.env.VUE_APP_API_URL;

const fetchItems = async (isLoadMore = false) => {
  if (!isLoadMore) {
    isLoading.value = true;
    page.value = 1;
    items.value = [];
  }

  const query = route.query.q || "";
  let url = `${prefix}/properties?page=${page.value}`;
  if (query) {
    url += `&q=${encodeURIComponent(query)}`;
  }

  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error("Network response was not ok");
    const data = await res.json();

    if (isLoadMore) {
      if (data.results) items.value.push(...data.results);
    } else {
      items.value = data.results || [];
      total.value = data.total || 0;
    }
  } catch (err) {
    console.error("Failed to fetch properties:", err);
    if (!isLoadMore) {
      items.value = [];
      total.value = 0;
    }
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchItems();
});

watch(
  () => route.query.q,
  () => {
    fetchItems();
  }
);

const resultFound = computed(() => {
  return (total.value || 0).toLocaleString();
});

const loadMore = async () => {
  page.value += 1;
  fetchItems(true);
};
</script>

<style scoped>
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
  width: 100%;
}
.listing-container {
  display: flex;
  flex-direction: column;
  min-height: 500px;
  padding: 40px 0;
  width: 100%;
}
ul {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  width: 100%;
  list-style-type: none;
  padding: 0;
  margin: 0;
}
.skeleton-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  width: 100%;
}
.skeleton-item {
  width: calc(33.33% - 16px);
}
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
  width: 100%;
}
.w-lg {
  padding: 0px 20px;
}
@media only screen and (max-width: 600px) {
  ul,
  .skeleton-grid {
    flex-direction: column;
  }
  ul li,
  .skeleton-item {
    width: 100% !important;
  }
}
@media only screen and (min-width: 600px) and (max-width: 991px) {
  ul li,
  .skeleton-item {
    width: calc(50% - 12px) !important;
  }
}
@media only screen and (min-width: 992px) {
  ul li,
  .skeleton-item {
    width: calc(33.33% - 16px) !important;
  }
}
</style>
