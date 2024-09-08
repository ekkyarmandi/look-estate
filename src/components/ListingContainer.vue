<template>
  <div class="wrapper listing-container">
    <ResultFound :total="resultFound"/>
    <div v-if:="isLoading">Loading</div>
    <ul v-if:="!isLoading">
      <li v-for:="item in items">
        <ListingItem :data="item" :key="item.id" />
      </li>
    </ul>
    <l-dot-pulse size="43" speed="1.3" color="#42b983"></l-dot-pulse>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue";
import ListingItem from "@/components/ListingItem.vue";
import ResultFound from "@/components/ResultFound.vue";

const items = ref([]);
const isLoading = ref(true);
const prefix = ref("");
const total = ref(0);

onMounted(() => {
  prefix.value = process.env.VUE_APP_API_URL;
});

onMounted(() => {
  const url = prefix.value + "/properties";
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      items.value.push(...data);
      isLoading.value = false;
      total.value += data.length;
    });
});

const resultFound = computed(()=>{
  return total.value.toLocaleString();
});

</script>

<style scoped>
.listing-container {
  margin-bottom: 40px;
  height: 100%;
}
ul {
  justify-content: space-between;
  width: 100%;
  list-style-type: none;
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
