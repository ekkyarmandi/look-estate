<template>
  <button type="button" :class="customClass" @click="$emit('click')"><slot /></button>
</template>

<script setup>
import { computed, defineProps, defineEmits } from "vue";

const props = defineProps(["class"]);
const emit = defineEmits(["click"]);

const customClass = computed(() => {
  return props.class;
});
</script>

<style>
button {
  min-width: 40px;
  min-height: 40px;
  font-size: 1rem;
  font-weight: bold;
  border: 0;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
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
.w-full {
  width: 100%;
}
</style>
