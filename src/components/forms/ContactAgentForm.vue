<template>
  <form id="contact-agent" class="">
    <div class="contact-info">
      <div class="img"></div>
      <div class="contact-detail">
        <p>Contact Name</p>
        <p><span>From: </span>Company Name</p>
      </div>
    </div>
    <Button class="btn-primary w-full">
      <WhatsAppIcon />
      <p>Contact Agent</p>
    </Button>
  </form>
</template>

<script>
import Button from "@/components/ui/Button.vue";
import WhatsAppIcon from "@/assets/icons/WhatsAppIcon.vue";
export default {
  name: 'ContactAgentForm',
  components: {
    Button,
    WhatsAppIcon,
  }
}
</script>

<style scoped>
.img {
  width: 100px;
  height: 100px;
  background-color: #d9d9d950;
  border-radius: 12px;
  border: 2px solid #d9d9d9;
}
.contact-info {
  display: flex;
  align-items: center;
  gap: 20px;
}
.contact-detail p:first-child {
  margin-bottom: 12px;
  font-weight: bold;
}
.contact-detail span {
  opacity: 0.5;
}
</style>
