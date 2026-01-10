<template>
  <div>
    <p>
      This website is part of
      <a href="https://www.ekky.dev">ekky.dev</a> portfolio
    </p>
  </div>
</template>

<script>
export default {
  name: "AppCopyright",
};
</script>

<style scoped>
div {
  background-color: var(--primary-500);
  width: 100%;
}
div p {
  color: white;
  font-size: 12px;
  padding: 8px 0;
  text-align: center;
}
div a {
  color: white;
}
</style>
