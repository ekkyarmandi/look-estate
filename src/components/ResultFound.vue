<template>
  <div class="result">
    <p>Sort By Price: Low to High</p>
    <p>
      <span>{{ total }}</span> Properties Found
    </p>
  </div>
</template>

<script setup>
import { computed, defineProps } from "vue";

const { total } = defineProps(["total"]);
</script>

<style scoped>
.result {
  display: flex;
  justify-content: space-between;
  padding: 12px 0;
}
.result {
  font-size: 14px;
  color: gray;
}
.result p span {
  font-weight: bold;
  color: var(--secondary-500);
}
</style>
