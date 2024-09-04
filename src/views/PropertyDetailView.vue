<template>
  <section>
    <div v-if:="isLoading" class="wrapper">Loading</div>
    <div v-if:="!isLoading" class="wrapper">
      <div class="content">
        <p>ID: {{ data.id }}</p>
        <div class="listing-title">
          <h1>{{ data.title }}</h1>
          <p>{{ data.priceUsd }}</p>
        </div>
        <div class="listing-id">
          <div class="listing-location">
            <LocationIcon />
            <p>{{ data.location }}</p>
          </div>
          <div class="btn-group">
            <Button class="box"><HearthIcon hideNumber="true" /></Button>
            <Button class="box btn-primary"><ShareIcon /></Button>
          </div>
        </div>
        <div class="image-container">
          <img v-if:="data.images.length > 0" :src="data.images[0]" :alt="'Thumbnail of ' + data.title" />
          <div class="image-options">
            <img v-for:="img in data.images" :src="img" :alt="'Thumbnail of ' + data.title" />
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

import { ref, computed, defineProps, onMounted } from "vue";

const props = defineProps(["id"]);
const prefix = "http://localhost:8000";

const data = ref({ id: props.id });
const isLoading = ref(true);

onMounted(() => {
  fetch(prefix + "/property/" + props.id)
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
</script>

<style scoped>
section {
  background-color: #d9d9d9;
}
.content > p {
  font-size: 18px;
}
.wrapper {
  padding: 20px 145px;
  display: flex;
  gap: 20px;
}
.content {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 43px 0;
}
.contact {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 43px 0;
}
.listing-title {
  display: flex;
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
.btn-group {
  display: flex;
  align-items: center;
  gap: 8px;
}
.image-container {
  width: 754px;
  overflow: hidden;
}
.image-container > img {
  width: 100%;
  border-radius: 8px;
  margin-bottom: 8px;
}
.image-options {
  overflow: scroll;
  display: flex;
  gap: 8px;
  overflow-x: hidden;
  overflow-y: hidden;
}
.image-options img {
  width: 150px;
  height: 112.5px;
  object-fit: cover;
}
</style>
