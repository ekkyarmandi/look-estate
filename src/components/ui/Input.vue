<template>
  <input type="text" :placeholder="placeholder"/>
</template>

<script>
export default {
  name: "Input",
  props: [ "placeholder" ]
}
</script>

<style>
input {
  font-size: 1rem;
  border: 1px solid #ccc;
  padding: 0 1rem;
  border-radius: 0.5rem;
  width: -webkit-fill-available;
  height: 40px;
}
</style>
