<template>
  <div class="listing-item">
    <Thumbnail :images="data.images" dotsClass="thumbnail">
      <div class="listing-location">
        <LocationIcon color="white" />
        <p>{{ data.location }}</p>
      </div>
      <div class="btn-like" @click="toggleBookmark">
        <BookmarkIcon :hideNumber="true" :color="isBookmarked ? '#42b983' : 'white'" :fill="isBookmarked ? '#42b983' : 'none'" />
      </div>
    </Thumbnail>
    <div class="title-wrapper">
      <a :href="'/properties/' + data.id">
        <h2>{{ data.title }}</h2>
      </a>
      <p class="price">{{ priceUsd }}</p>
    </div>
    <div class="badges">
      <Badge>
        <ScriptIcon />
        <p>{{ data.hold_type }}</p>
      </Badge>
      <Badge>
        <HouseIcon />
        <p>{{ data.property_type }}</p>
      </Badge>
      <Badge v-if:="!noBedroom">
        <BedIcon />
        <p>{{ data.bedrooms }}</p>
      </Badge>
      <Badge v-if:="!noBathroom">
        <BathIcon />
        <p>{{ data.bathrooms }}</p>
      </Badge>
      <Badge v-if:="!noBuildSize">
        <BuildingIcon />
        <p>{{ buildingSize }} sqm</p>
      </Badge>
      <Badge v-if:="!noLandSize">
        <AreaIcon />
        <p>{{ landSize }} sqm</p>
      </Badge>
    </div>
  </div>
</template>

<script setup>
import Badge from "@/components/Badge.vue";
import Thumbnail from "@/components/Thumbnail.vue";
import HashIcon from "@/assets/icons/HashIcon.vue";
import BedIcon from "@/assets/icons/BedIcon.vue";
import BathIcon from "@/assets/icons/BathIcon.vue";
import BuildingIcon from "@/assets/icons/BuildingIcon.vue";
import AreaIcon from "@/assets/icons/AreaIcon.vue";
import ScriptIcon from "@/assets/icons/ScriptIcon.vue";
import LeftIcon from "@/assets/icons/LeftIcon.vue";
import RightIcon from "@/assets/icons/RightIcon.vue";
import LocationIcon from "@/assets/icons/LocationIcon.vue";
import BookmarkIcon from "@/assets/icons/BookmarkIcon.vue";
import HouseIcon from "@/assets/icons/HouseIcon.vue";
import { useBookmarkStore } from "@/store/bookmark";
import { storeToRefs } from "pinia";

import { computed, defineProps } from "vue";

const { data } = defineProps(["data"]);
const bookmarkStore = useBookmarkStore();
const { bookmarked } = storeToRefs(bookmarkStore);

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

const noBedroom = computed(() => {
  return !data.bedrooms;
});

const noBathroom = computed(() => {
  return !data.bathrooms;
});

const noBuildSize = computed(() => {
  return !data.build_size;
});

const noLandSize = computed(() => {
  return !data.land_size;
});

const isBookmarked = computed(() => {
  return bookmarked.value.includes(data);
});

function toggleBookmark() {
  if (bookmarked.value.includes(data)) {
    bookmarkStore.removeBookmark(data);
  } else {
    bookmarkStore.addBookmark(data);
  }
}
</script>

<style scoped>
.listing-item {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

h2 {
  font-size: 20px;
}

.title-wrapper {
  display: flex;
  justify-content: space-between;
  color: var(--secondary-500);
  gap: 8px;
  /* height: 50px; */
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

.listing-location,
.btn-like {
  z-index: 10;
}
</style>
