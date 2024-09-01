<template>
  <button type="button" :class="{ 'icon-only': iconOnly }" :style="buttonStyle">
    <slot />
  </button>
</template>

<script>
export default {
  name: "Button",
  props: ["iconOnly", "backgroundColor"],
  computed: {
    buttonStyle() {
      return {
        backgroundColor: this.backgroundColor,
        border: this.backgroundColor === "#fff" ? "1px solid #ccc" : "none",
      };
    },
  },
};
</script>

<style scoped>
button {
  height: 40px;
  width: 100px;
  border-radius: 8px;
  color: white;
  font-weight: 600;
  background: var(--primary-500);
}
button:hover {
  background: var(--primary-600);
}
button.icon-only {
  height: 40px;
  width: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
}
</style>
