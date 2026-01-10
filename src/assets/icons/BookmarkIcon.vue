<template>
  <div v-if="!hideNumber" class="whistlist">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M19 21L12 17L5 21V5C5 4.46957 5.21071 3.96086 5.58579 3.58579C5.96086 3.21071 6.46957 3 7 3H17C17.5304 3 18.0391 3.21071 18.4142 3.58579C18.7893 3.96086 19 4.46957 19 5V21Z"
        :stroke="color"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
    <div>
      <p>{{ bookmark.total }}</p>
    </div>
  </div>
  <div v-if="hideNumber" :class="['heart-icon', { 'custom-color': !color }]">
    <svg width="24" height="24" viewBox="0 0 24 24" :fill="fill" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M19 21L12 17L5 21V5C5 4.46957 5.21071 3.96086 5.58579 3.58579C5.96086 3.21071 6.46957 3 7 3H17C17.5304 3 18.0391 3.21071 18.4142 3.58579C18.7893 3.96086 19 4.46957 19 5V21Z"
        :stroke="color"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
  </div>
</template>

<script setup>
import { useBookmarkStore } from "@/store/bookmark";

defineProps({
  hideNumber: {
    type: Boolean,
    default: false,
  },
  color: {
    type: String,
    default: "#30485E",
  },
  fill: {
    type: String,
    default: "none",
  },
});

const bookmark = useBookmarkStore();
</script>

<style scoped>
.custom-color {
  --path-stroke: var(--secondary-500);
}
.cutom-color:hover {
  --path-stroke: var(--secondary-400);
}
.custom-color svg path {
  stroke: var(--path-stroke);
}
.whistlist {
  position: relative;
  margin-right: 0.5rem;
  cursor: pointer;
  width: 33px;
  height: 30px;
}
.whistlist svg {
  position: absolute;
  left: 0;
  bottom: 0;
}
.whistlist div {
  position: absolute;
  top: 0;
  right: 0;
}
.whistlist p {
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--primary-500);
  color: white;
  width: 18px;
  height: 18px;
  font-size: 12px;
  border: 1px solid white;
  border-radius: 50%;
}
.heart-icon {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
