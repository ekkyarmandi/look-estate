<template>
  <input @change.prevent="$emit('change', $event)" :value="value" type="text" :placeholder="placeholder" />
</template>

<script setup>

import { defineProps,defineEmits } from "vue";

const { placeholder,value } = defineProps(["placeholder","value"]);
const emit = defineEmits(["change"]);

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
