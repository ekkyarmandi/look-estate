<template>
  <div class="listing-item">
    <div class="thumbnail-container">
      <ul class="dots">
        <li :key="idx" v-for:="(_, idx) in data.images.slice(0, 15)" :class="activeDot == idx ? 'dot active' : 'dot'" @click="handleThumbnailChanges(idx, $event)"></li>
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
      <div class="listing-location">
        <LocationIcon color="white" />
        <p>{{ data.location }}</p>
      </div>
      <div class="btn-like">
        <HearthIcon :hideNumber="true" color="white" />
      </div>
      <div class="images">
        <img :key="idx" v-for="(img, idx) in data.images.slice(0, 15)" :class="'thumbnail-image ' + (activeIdx != idx && 'hidden')" :data-index="activeIdx == idx ? 0 : -1" :src="img" />
      </div>
    </div>
    <div class="title-wrapper">
      <a :href="'/properties/' + data.id">
        <h2>{{ data.title }}</h2>
      </a>
      <p class="price">{{ priceUsd }}</p>
    </div>
    <div class="badges">
      <Badge>
        <HashIcon />
        <p>{{ data.id }}</p>
      </Badge>
      <Badge>
        <BedIcon />
        <p>{{ data.bedrooms }}</p>
      </Badge>
      <Badge>
        <BathIcon />
        <p>{{ data.bathrooms }}</p>
      </Badge>
      <Badge>
        <BuildingIcon />
        <p>{{ buildingSize }} sqm</p>
      </Badge>
      <Badge>
        <AreaIcon />
        <p>{{ landSize }} sqm</p>
      </Badge>
      <Badge>
        <ScriptIcon />
        <p>{{ data.hold_type }}</p>
      </Badge>
    </div>
  </div>
</template>

<script setup>
import Badge from "@/components/Badge.vue";
import HashIcon from "@/assets/icons/HashIcon.vue";
import BedIcon from "@/assets/icons/BedIcon.vue";
import BathIcon from "@/assets/icons/BathIcon.vue";
import BuildingIcon from "@/assets/icons/BuildingIcon.vue";
import AreaIcon from "@/assets/icons/AreaIcon.vue";
import ScriptIcon from "@/assets/icons/ScriptIcon.vue";
import LeftIcon from "@/assets/icons/LeftIcon.vue";
import RightIcon from "@/assets/icons/RightIcon.vue";
import LocationIcon from "@/assets/icons/LocationIcon.vue";
import HearthIcon from "@/assets/icons/HearthIcon.vue";

import { ref, computed, defineProps } from "vue";

const { data } = defineProps(["data"]);

const activeIdx = ref(0);
const activeDot = ref(0);
const actionClass = ref("");

const priceUsd = computed(() => {
  return data.price
    .toLocaleString("en-US", {
      style: "currency",
      currency: "USD",
    })
    .replace(".00", "");
});

const buildingSize = computed(() => {
  return data.build_size.toLocaleString("en-US");
});

const landSize = computed(() => {
  return data.land_size.toLocaleString("en-US");
});

// Carousel
const handleThumbnailChanges = (idx, event) => {
  const imagesLen = data.images.length < 15 ? data.images.length : 15;
  const thumbnailContainer = event.target.closest("div.thumbnail-container");
  const images = thumbnailContainer.querySelectorAll(".images img");

  if (idx < 0) {
    idx = imagesLen - 1;
    images[imagesLen - 1].classList.remove("hidden");
    activeDot.value = imagesLen - 1;
    setTimeout(() => {
      activeIdx.value = imagesLen - 1;
    }, 300);
  } else if (idx >= imagesLen) {
    idx = 0;
    images[0].classList.remove("hidden");
    activeDot.value = 0;
    setTimeout(() => {
      activeIdx.value = 0;
    }, 300);
  }
  images.forEach((e, i) => {
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
.listing-item {
  width: 427px;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.listing-item img {
  height: 320px;
  border-radius: 8px;
}

h2 {
  font-size: 20px;
}

.title-wrapper {
  display: flex;
  justify-content: space-between;
  color: var(--secondary-500);
  gap: 8px;
}

.title-wrapper a {
  text-decoration: none;
  color: inherit;
}

.title-wrapper a:hover {
  text-decoration: underline;
  color: inherit;
}

.price {
  font-size: 18px;
  font-weight: 600;
}

.badges {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}

.badges p {
  font-size: 1rem;
}

/* Thumbnail */
.thumbnail-container {
  position: relative;
  aspect-ratio: 4/3;
  height: 320px;
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

.dots {
  position: absolute;
  top: 238px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 6px;
  list-style: none;
  cursor: pointer;
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
}

.btn-circle:hover {
  background-color: #ffffff80;
}

.listing-location {
  display: flex;
  position: absolute;
  bottom: 8px;
  left: 8px;
  align-items: center;
  background-color: #ffffff60;
  color: #fff;
  border-radius: 4px;
  padding: 8px;
  gap: 4px;
}

.listing-location p {
  text-transform: uppercase;
}

.btn-like {
  position: absolute;
  top: 5%;
  right: 5%;
  border-radius: 100%;
  cursor: pointer;
}
.dots,
.btn-group,
.listing-location,
.btn-like {
  z-index: 10;
}
</style>
