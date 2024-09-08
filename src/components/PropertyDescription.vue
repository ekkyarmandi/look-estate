<template>
  <div class="description-wrapper">
    <h2>Description</h2>
    <div class="content">{{ description }}</div>
  </div>
</template>

<script>
export default {
  name: "PropertyDescription",
  props: ["description"],
};
</script>

<style scoped>
.description-wrapper {
  padding: 28px;
  border-radius: 12px;
  background-color: white;
  color: var(--secondary-500);
}
h2 {
  font-size: 24px;
  margin-bottom: 24px;
}
.content {
  font-size: 16px;
  line-height: 28px;
}

@media screen and (max-width: 600px){
  h2 {
    font-size: 20px;
    margin-bottom: 1rem;
  }
}
</style>
