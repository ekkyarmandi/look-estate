<template>
  <section>
    <div v-if:="isLoading" class="wrapper">Loading</div>
    <div v-if:="!isLoading" class="wrapper">
      <div class="content">
        <p>ID: {{ data.id }}</p>
        <div class="listing-title">
          <h1>{{ data.title }}</h1>
          <p>{{ priceUsd }}</p>
        </div>
        <div class="listing-id">
          <div class="listing-location">
            <LocationIcon />
            <p>{{ data.location }}</p>
          </div>
          <div class="btns">
            <Button class="box"><HearthIcon hideNumber="true" /></Button>
            <Button class="box btn-primary"><ShareIcon /></Button>
          </div>
        </div>
        <div class="image-container">
          <Thumbnail :images="data.images" style="width: 754px;" dotsClass="property" />
          <div
            class="image-options"
            ref="imageOptions"
            @mousedown="onMouseDown"
            @mousemove="onMouseMove"
            @mouseup="onMouseUp"
            @mouseleave="onMouseLeave"
          >
            <img
              v-for:="img in data.images.slice(0, 15)"
              :src="img"
              :alt="'Thumbnail of ' + data.title"
            />
          </div>
        </div>
        <PropertyDetail :data="data" />
        <PropertyDescription :description="data.description" />
      </div>
      <div class="contact">
        <GetInTouchForm />
        <ContactAgentForm :data="data.agent" />
      </div>
    </div>
  </section>
</template>

<script setup>
import GetInTouchForm from "@/components/forms/GetInTouchForm.vue";
import ContactAgentForm from "@/components/forms/ContactAgentForm.vue";
import PropertyDetail from "@/components/PropertyDetail.vue";
import PropertyDescription from "@/components/PropertyDescription.vue";
import HearthIcon from "@/assets/icons/HearthIcon.vue";
import LocationIcon from "@/assets/icons/LocationIcon.vue";
import ShareIcon from "@/assets/icons/ShareIcon.vue";
import LeftIcon from "@/assets/icons/LeftIcon.vue";
import RightIcon from "@/assets/icons/RightIcon.vue";
import Thumbnail from "@/components/Thumbnail.vue";

import { ref, computed, defineProps, onMounted } from "vue";

const props = defineProps(["id"]);
const prefix = ref("");

const data = ref({ id: props.id, images: [] });
const isLoading = ref(true);

onMounted(() => {
  prefix.value = process.env.VUE_APP_API_URL;
});

onMounted(() => {
  fetch(prefix.value + "/property/" + props.id)
    .then((res) => res.json())
    .then((result) => {
      data.value = result;
      isLoading.value = false;
    })
    .catch((err) => console.log(err));
});

const priceUsd = computed(() => {
  return data.value.price
    .toLocaleString("en-US", {
      style: "currency",
      currency: "USD",
    })
    .replace(".00", "");
});

// scroll image options
const isDragging = ref(false);
const startX = ref(0);
const scrollLeft = ref(0);
const imageOptions = ref(null);
function onMouseDown(event) {
  event.preventDefault();
  isDragging.value = true;
  startX.value = event.pageX - imageOptions.value.offsetLeft;
  scrollLeft.value = imageOptions.value.scrollLeft;
}
function onMouseMove(event) {
  if (!isDragging.value) return;
  event.preventDefault();
  const x = event.pageX - imageOptions.value.offsetLeft;
  const walk = (x - startX.value) * 1; // Adjust the scroll speed
  imageOptions.value.scrollLeft = scrollLeft.value - walk;
}
function onMouseUp() {
  isDragging.value = false;
}
function onMouseLeave() {
  isDragging.value = false;
}

</script>

<style scoped>
section {
  background-color: #d9d9d9;
}

.wrapper {
  padding: 20px;
  gap: 20px;
  display: flex;
  justify-content: center;
  max-width: 1440px;
}

/* Content */
.content {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 43px 0;
  /* max-width: 747px; */
}


.content > p {
  font-size: 18px;
}

.listing-title {
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 8px;
}

.listing-title h1 {
  font-size: 32px;
  font-weight: bold;
}

.listing-title p {
  font-size: 28px;
}

.listing-id {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.listing-location {
  display: flex;
  align-items: center;
  gap: 8px;
}

.listing-location p {
  font-size: 18px;
}

.btns {
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Contact */
.contact {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 43px 0;
  /* max-width: 311px; */
}

/* Thumbnail Images */
.image-container {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  gap: 8px;
}

.image-container img {
  width: 100%;
  border-radius: 8px;
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

.image-options {
  display: flex;
  overflow-x: scroll;
  cursor: grab;
  gap: 8px;
}

.image-options:active {
  cursor: grabbing;
}

.image-options img {
  width: 150px;
  height: 112.5px;
  object-fit: cover;
  user-select: none;
}


@media screen and (max-width: 600px){
  .listing-title, .wrapper, .content, .contact {
    row-gap: 12px;
  }
  .listing-title {
    display: flex;
    flex-direction: column;
  }
  .wrapper {
    display: flex;
    flex-direction: column;
  }
  .content,.contact {
    padding-top: 0; 
    padding-bottom: 0; 
  }
  .image-container .image-options {
    display: none;
  }
  .contact {
    display: grid;
  }
  .contact form:first-child {
    order: 2;
  }
  .contact form:nth-child(2) {
    order: 1;
  }
}

@media screen and (min-width: 600px){
  .wrapper {
    display: flex;
    flex-direction: column;
    padding: 20px;
  }
  .content {
    padding-top: 0; 
    padding-bottom: 0; 
  }
  .contact {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    padding-top: 0; 
    padding-bottom: 0; 
  }
}

@media screen and (min-width: 992px){
  .content {
    max-width: 65%;
  }
  .contact {
    width: 300px;
  }
}

@media screen and (min-width: 1200px){
  .content {
    max-width: 747px;
  }
  .contact {
    width: 320px;
  }
}
</style>
