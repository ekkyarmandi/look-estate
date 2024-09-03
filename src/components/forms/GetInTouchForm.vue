<template> 
  <form id="getInTouch">
    <h2>Get In Touch</h2>
    <div>
      <label for="name">Name</label>
      <Input />
    </div>
    <div>
      <label for="email">Email</label>
      <Input />
    </div>
    <div>
      <label for="message">Message</label>
      <textarea placeholder="type your message here"></textarea>
    </div>
    <Button class="btn-primary w-full">Send</Button>
  </form>
</template> 

<script>
import Input from "@/components/ui/Input.vue";
import Button from "@/components/ui/Button.vue";
export default {
  name: 'GetInTouchForm',
  components: {
    Input,
    Button,
  }
}
</script>

<style scoped>
h2 {
  font-size: 1.25rem;
  font-weight: bold;
  text-align: center;
}
label {
  display: inline-block;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 12px;
  width: fit-content;
}
textarea {
  font-size: 1rem;
  border: 1px solid #ccc;
  padding: 1rem;
  border-radius: 0.5rem;
  height: 120px;
  width: -webkit-fill-available;
}
</style>
