<template>
  <div><slot/></div>
</template>

<script>
export default {
  name: "Badge",
}
</script>

<style scoped>
div {
  display: flex;
  gap: 4px;
  padding: 4px 8px;
  border: 1px solid #ccc;
  border-radius: 8px;
  width: fit-content;
  color: var(--secondary-500);
}
</style>
