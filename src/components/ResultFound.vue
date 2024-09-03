<template>
  <div class="wrapper">
    <div class="result">
      <p>Sort By Price: Low to High</p>
      <p><span>10</span> Properties Found</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "ResultFound",
};
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
