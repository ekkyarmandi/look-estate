<template>
  <div class="wrapper listing-container">
    <div v-if:="isLoading">Loading</div>
    <ul v-if:="!isLoading">
      <li v-for:="item in items">
        <ListingItem :data="item" :key="item.id"/>
      </li>
    </ul>
    <l-dot-pulse size="43" speed="1.3" color="#42b983"></l-dot-pulse>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import ListingItem from "@/components/ListingItem.vue";

const items = ref([]);
const isLoading = ref(true);

onMounted(()=>{
  const url = "http://localhost:8000/properties";
  fetch(url).then((res)=>res.json()).then((data)=>{
    items.value.push(...data);
    isLoading.value = false;
  });
});
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
