<template>
  <Transition name="slide-fade">
    <div v-if="show" class="auth-popover-container">
      <!-- Transparent backdrop to catch clicks outside -->
      <div class="popover-overlay" @click="$emit('close')"></div>

      <div class="auth-card">
        <button class="close-btn" @click="$emit('close')">&times;</button>
        <h2 class="title">Join Us</h2>

        <div class="form-container">
          <form @submit.prevent="handleSubmit">
            <div class="form-group">
              <label>Full Name</label>
              <Input
                type="text"
                placeholder="Example User"
                v-model:value="form.fullName"
              />
            </div>

            <div class="form-group">
              <label>Email</label>
              <Input
                type="email"
                placeholder="example@mail.com"
                v-model:value="form.email"
              />
            </div>

            <div class="form-group">
              <label>Password</label>
              <div class="input-wrapper">
                <Input
                  :type="showPassword ? 'text' : 'password'"
                  placeholder="••••••••"
                  v-model:value="form.password"
                />
                <button
                  type="button"
                  class="toggle-password"
                  @click="showPassword = !showPassword"
                >
                  <svg
                    v-if="showPassword"
                    xmlns="http://www.w3.org/2000/svg"
                    width="20"
                    height="20"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path
                      d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"
                    ></path>
                    <circle cx="12" cy="12" r="3"></circle>
                  </svg>
                  <svg
                    v-else
                    xmlns="http://www.w3.org/2000/svg"
                    width="20"
                    height="20"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path
                      d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"
                    ></path>
                    <line x1="1" y1="1" x2="23" y2="23"></line>
                  </svg>
                </button>
              </div>
            </div>

            <div class="form-group">
              <label>Retype Password</label>
              <div class="input-wrapper">
                <Input
                  :type="showRetypePassword ? 'text' : 'password'"
                  placeholder="password"
                  v-model:value="form.retypePassword"
                />
                <button
                  type="button"
                  class="toggle-password"
                  @click="showRetypePassword = !showRetypePassword"
                >
                  <svg
                    v-if="showRetypePassword"
                    xmlns="http://www.w3.org/2000/svg"
                    width="20"
                    height="20"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path
                      d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"
                    ></path>
                    <circle cx="12" cy="12" r="3"></circle>
                  </svg>
                  <svg
                    v-else
                    xmlns="http://www.w3.org/2000/svg"
                    width="20"
                    height="20"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path
                      d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"
                    ></path>
                    <line x1="1" y1="1" x2="23" y2="23"></line>
                  </svg>
                </button>
              </div>
            </div>

            <Button type="submit" class="btn-register full-width"
              >Register</Button
            >
          </form>
        </div>

        <div class="social-auth">
          <div class="divider">
            <span>or</span>
          </div>
          <button class="google-btn">
            <img
              src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg"
              alt="Google"
              width="18"
              height="18"
            />
            Join using Google
          </button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, reactive } from "vue";
import Input from "./Input.vue";
import Button from "./Button.vue";

defineProps({
  show: Boolean,
});

const emit = defineEmits(["close"]);

const showPassword = ref(false);
const showRetypePassword = ref(false);

const form = reactive({
  fullName: "",
  email: "",
  password: "",
  retypePassword: "",
});

const handleSubmit = () => {
  console.log("Form submitted:", form);
  emit("close");
};
</script>

<style scoped>
.auth-popover-container {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 12px;
  z-index: 1000;
}

.popover-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1;
}

.auth-card {
  background: white;
  padding: 20px;
  border-radius: 20px;
  position: relative;
  width: 380px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
  border: 1px solid #eee;
}

.close-btn {
  position: absolute;
  top: 1rem;
  right: 1.25rem;
  background: none;
  border: none;
  font-size: 1.25rem;
  cursor: pointer;
  color: #2a435d;
  font-weight: 300;
  line-height: 1;
  transition: opacity 0.2s;
}

.close-btn:hover {
  opacity: 0.7;
}

.title {
  text-align: center;
  font-size: 1.25rem;
  font-weight: 700;
  color: #2a435d;
  margin-bottom: 0.25rem;
}

.form-group {
  margin-bottom: 0.75rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.25rem;
  font-weight: 600;
  font-size: 0.85rem;
  color: #2a435d;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.toggle-password {
  position: absolute;
  right: 0.75rem;
  background: none;
  border: none;
  cursor: pointer;
  color: #94a3b8;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
}

.toggle-password:hover {
  color: #64748b;
}

.btn-register {
  background-color: #40b589;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  margin-top: 0.5rem;
  transition: background-color 0.2s;
  cursor: pointer;
}

.btn-register:hover {
  background-color: #36a279;
}

.full-width {
  width: 100%;
}

.divider {
  position: relative;
  text-align: center;
  margin: 0.75rem 0;
}

.divider span {
  position: relative;
  background: white;
  padding: 0 10px;
  font-size: 0.9rem;
  color: #2a435d;
}

.google-btn {
  width: 100%;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
  background-color: #edf0f3;
  color: #2a435d;
  font-weight: 500;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.google-btn:hover {
  background-color: #e2e8f0;
}

/* Transitions: Fade in from top */
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.2s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from {
  transform: translateY(-20px);
  opacity: 0;
}
.slide-fade-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}

:deep(input) {
  border: 1px solid #cbd5e1;
  color: #2a435d;
  height: 34px !important;
  font-size: 0.9rem;
}

:deep(input:focus) {
  border-color: #40b589;
  outline: none;
  box-shadow: 0 0 0 2px rgba(64, 181, 137, 0.1);
}

@media only screen and (max-width: 600px) {
  .auth-card {
    width: 90vw;
    right: -20px; /* Offset to keep it centered on mobile if needed, or adjust alignment */
  }
}
</style>
