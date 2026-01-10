<template>
  <input
    @change.prevent="$emit('change', $event)"
    @input="$emit('update:value', $event.target.value)"
    :value="value"
    :type="type || 'text'"
    :placeholder="placeholder"
  />
</template>

<script setup>
import { defineProps, defineEmits } from "vue";

defineOptions({
  name: "AppInput",
});

const { placeholder, value, type } = defineProps([
  "placeholder",
  "value",
  "type",
]);
defineEmits(["change", "update:value"]);
</script>

<style>
input {
  font-size: 1rem;
  border: 1px solid #ccc;
  padding: 0 1rem;
  border-radius: 0.5rem;
  width: -webkit-fill-available;
  height: 38px;
}
</style>
