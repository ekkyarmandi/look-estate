<template>
  <form id="contact-agent" class="">
    <div class="contact-info">
      <img :src="data.photograph" :alt="data.name" />
      <div class="contact-detail">
        <p>{{ data.name }}</p>
        <p><span>From: </span>{{ data.company }}</p>
      </div>
    </div>
    <a :href="data.whatsapp">
      <Button class="btn-primary w-full">
        <WhatsAppIcon />
        <p>Contact Agent</p>
      </Button>
    </a>
  </form>
</template>

<script setup>
import Button from "@/components/ui/Button.vue";
import WhatsAppIcon from "@/assets/icons/WhatsAppIcon.vue";

import { defineProps } from "vue";

const { data } = defineProps(["data"]);
</script>

<style scoped>
img {
  width: 110px;
  height: 110px;
  border-radius: 12px;
  object-fit: cover;
  object-position: top;
}
.contact-info {
  display: flex;
  align-items: center;
  gap: 16px;
}
.contact-detail p:first-child {
  margin-bottom: 12px;
  font-weight: bold;
}
.contact-detail span {
  opacity: 0.5;
}
a {
  text-decoration: none;
}
p {
  font-size: 14px;
}
#contact-agent {
  height: fit-content;
}
</style>
