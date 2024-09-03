<template>
  <div class="listing-item">
    <div class="thumbnail-container">
      <img class="thumbnail-image" src="@/assets/thumbnail.png" :alt="'Thumbnail of ' + data.title" />
      <ul class="dots">
        <li class="dot active"></li>
        <li v-for:="dot in data.dots" class="dot"></li>
      </ul>
      <div class="btn-container">
        <div class="btn-group">
          <button class="btn-circle"><LeftIcon /></button>
          <button class="btn-circle"><RightIcon /></button>
        </div>
      </div>
      <div class="listing-location">
        <LocationIcon color="white" />
        <p>{{ data.location }}</p>
      </div>
      <div class="btn-like">
        <HearthIcon hideNumber="true" color="white" />
      </div>
    </div>
    <div class="title-wrapper">
      <h2>{{ data.title }}</h2>
      <p class="price">{{ data.price_usd }}</p>
    </div>
    <div class="badges">
      <Badge
        ><HashIcon />
        <p>{{ data.id }}</p></Badge
      >
      <Badge
        ><BedIcon />
        <p>{{ data.bedrooms }}</p></Badge
      >
      <Badge
        ><BathIcon />
        <p>{{ data.bathrooms }}</p></Badge
      >
      <Badge
        ><BuildingIcon />
        <p>{{ data.buildingSize }} sqm</p></Badge
      >
      <Badge
        ><AreaIcon />
        <p>{{ data.landSize }} sqm</p></Badge
      >
      <Badge
        ><ScriptIcon />
        <p>{{ data.contract_type }}</p></Badge
      >
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

import { ref, computed } from "vue";

const data = ref({
  id: "436393",
  title: "Charming One Bedroom Villa in Ubud with A Spacious Garden",
  location: "Ubud, Bali",
  contract_type: "Leasehold",
  price: 10000,
  bedrooms: 2,
  bathrooms: 2,
  building_size: 1234,
  land_size: 1234,
  dots: [1, 2, 3, 4],
});

const price_usd = computed(() => {
  return data.value.price
    .toLocaleString("en-US", {
      style: "currency",
      currency: "USD",
    })
    .replace(".00", "");
});

const buildingSize = computed(() => {
  return data.value.building_size.toLocaleString("en-US");
});

const landSize = computed(() => {
  return data.value.land_size.toLocaleString("en-US");
});
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
  height: 320px;
}
.dots {
  position: absolute;
  top: 238px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 6px;
  list-style: none;
  z-index: 10;
  cursor: pointer;
}
.dot {
  width: 10px;
  height: 10px;
  border-radius: 100%;
  background-color: #d9d9d9;
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
</style>
