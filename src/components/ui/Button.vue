<template>
  <button type="button" :class="btnClass"><slot /></button>
</template>

<script>
export default {
  name: "Button",
  props: ["class"],
  computed: {
    btnClass() {
      return this.class;
    },
  },
};
</script>

<style>
button {
  width: 100px;
  height: 40px;
  font-size: 1rem;
  font-weight: bold;
  border: 0;
  border-radius: 0.5rem;
  cursor: pointer;
}
.btn-primary {
  background-color: var(--primary-500);
  color: white;
}
.btn-primary:hover {
  background-color: var(--primary-600);
}
.btn-light {
  border: 1px solid #ccc;
  background-color: white;
}
.box {
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
}
</style>
