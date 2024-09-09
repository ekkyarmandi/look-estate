<template>
  <div class="thumbnail-container">
    <div class="images">
      <img :key="idx" v-for="(img, idx) in thumbnails" :class="'thumbnail-image ' + (activeIdx != idx && 'hidden')" :data-index="activeIdx == idx ? 0 : -1" :src="img" />
    </div>
    <ul :class="'dots ' + dotsClass">
      <li :key="idx" v-for:="(_, idx) in thumbnails" :class="activeDot == idx ? 'dot active' : 'dot'" @click="handleThumbnailChanges(idx, $event)"></li>
    </ul>
    <div class="btn-container">
      <div class="btn-group">
        <button class="btn-circle" @click="handleThumbnailChanges(activeIdx - 1, $event)">
          <LeftIcon />
        </button>
        <button class="btn-circle" @click="handleThumbnailChanges(activeIdx + 1, $event)">
          <RightIcon />
        </button>
      </div>
    </div>
    <slot />
  </div>
</template>

<script setup>
import LeftIcon from "@/assets/icons/LeftIcon.vue";
import RightIcon from "@/assets/icons/RightIcon.vue";

import { ref, computed, defineProps } from "vue";

const { images, style, dotsClass } = defineProps(["images", "style", "dotsClass"]);

const activeIdx = ref(0);
const activeDot = ref(0);

const thumbnails = computed(() => {
  return images.slice(0, 15);
});

const handleThumbnailChanges = (idx, event) => {
  const imgLen = images.length < 15 ? images.length : 15;
  const thumbnailContainer = event.target.closest("div.thumbnail-container");
  const imageList = thumbnailContainer.querySelectorAll(".images img");
  if (idx < 0) {
    idx = imgLen - 1;
  } else if (idx >= imgLen) {
    idx = 0;
  }
  imageList.forEach((e, i) => {
    if (activeIdx.value == idx) return;
    if (idx == i) {
      e.classList.remove("hidden");
    }
    if (activeIdx.value == i) {
      activeDot.value = idx;
      e.classList.add("out");
      setTimeout(() => {
        e.classList.add("hidden");
        e.classList.remove("out");
        activeIdx.value = idx;
      }, 300);
    }
  });
};
</script>

<style scoped>
img {
  border-radius: 8px;
}

.thumbnail-container {
  position: relative;
  aspect-ratio: 4/3;
  overflow: hidden;
  border-radius: 12px;
}

.images img {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 0;
}

.images img[data-index="0"] {
  z-index: 1;
}

.thumbnail-image {
  object-fit: cover;
  width: 100%;
  height: 100%;
}

.thumbnail-image.out {
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
}

.thumbnail-image.hidden {
  display: none;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 100%;
  background-color: #fff;
  opacity: 0.5;
}

.dot.active {
  opacity: 1;
}

.dot:hover {
  background-color: #fff;
  opacity: 1;
}

.btn-container {
  position: absolute;
  top: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.btn-group {
  width: 93%;
  flex-shrink: 0;
  display: flex;
  justify-content: space-between;
}

.btn-circle {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 100%;
  background-color: #ffffff50;
  border: 0;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
}

.btn-circle svg {
  opacity: 50%;
}

.btn-circle:hover {
  background-color: #ffffff80;
}

.dots,
.btn-group {
  z-index: 10;
}
</style>
