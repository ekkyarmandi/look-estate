<template>
  <div class="empty-state">
    <div class="animation-container">
      <div class="box-animation">
        <svg
          width="120"
          height="120"
          viewBox="0 0 120 120"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <!-- Box Shadow -->
          <ellipse
            class="box-shadow"
            cx="60"
            cy="100"
            rx="30"
            ry="8"
            fill="rgba(0,0,0,0.05)"
          />

          <g class="box-content">
            <!-- Box Body -->
            <path
              d="M30 45L60 30L90 45V75L60 90L30 75V45Z"
              fill="#F3F4F6"
              stroke="#D1D5DB"
              stroke-width="2"
            />
            <!-- Inner Sides -->
            <path d="M30 45L60 60L90 45" stroke="#D1D5DB" stroke-width="2" />
            <path d="M60 60V90" stroke="#D1D5DB" stroke-width="2" />

            <!-- Floating Elements (representing "empty" but active) -->
            <rect
              class="float-item-1"
              x="45"
              y="40"
              width="8"
              height="2"
              rx="1"
              fill="#D1D5DB"
            />
            <rect
              class="float-item-2"
              x="65"
              y="50"
              width="12"
              height="2"
              rx="1"
              fill="#E5E7EB"
            />
            <rect
              class="float-item-3"
              x="50"
              y="65"
              width="10"
              height="2"
              rx="1"
              fill="#E5E7EB"
            />
          </g>
        </svg>
      </div>
    </div>
    <h2>No Properties Found</h2>
    <p>
      We couldn't find any listings matching your criteria. Try adjusting your
      filters or search something else.
    </p>
    <Button class="btn-primary" @click="resetSearch"
      >Explore All Properties</Button
    >
  </div>
</template>

<script setup>
import Button from "@/components/ui/Button.vue";
import { useRouter } from "vue-router";

const router = useRouter();

const resetSearch = () => {
  router.push({ path: "/" });
};
</script>

<style scoped>
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 80px 20px;
  text-align: center;
  width: 100%;
  min-height: 450px;
  background-color: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 24px;
}

.animation-container {
  margin-bottom: 40px;
  perspective: 1000px;
}

.box-animation {
  animation: float 4s ease-in-out infinite;
}

.box-content {
  animation: subtle-rotate 8s linear infinite;
  transform-origin: center;
}

.box-shadow {
  animation: shadow-scale 4s ease-in-out infinite;
  transform-origin: center;
}

.float-item-1 {
  animation: drift 3s ease-in-out infinite;
}
.float-item-2 {
  animation: drift 4s ease-in-out infinite 0.5s;
}
.float-item-3 {
  animation: drift 5s ease-in-out infinite 1s;
}

@keyframes float {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-15px);
  }
}

@keyframes shadow-scale {
  0%,
  100% {
    transform: scale(1);
    opacity: 0.5;
  }
  50% {
    transform: scale(0.8);
    opacity: 0.2;
  }
}

@keyframes subtle-rotate {
  0% {
    transform: rotateY(0deg);
  }
  100% {
    transform: rotateY(360deg);
  }
}

@keyframes drift {
  0%,
  100% {
    transform: translate(0, 0);
    opacity: 0;
  }
  25% {
    opacity: 1;
  }
  75% {
    opacity: 1;
  }
  100% {
    transform: translate(0, -20px);
    opacity: 0;
  }
}

h2 {
  font-size: 28px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 16px;
  letter-spacing: -0.025em;
}

p {
  font-size: 17px;
  color: #6b7280;
  max-width: 440px;
  margin-bottom: 40px;
  line-height: 1.6;
}

.btn-primary {
  padding: 14px 40px;
  font-weight: 600;
  border-radius: 12px;
  transition: all 0.2s ease;
  background-color: #1f2937;
  color: white;
  border: none;
  cursor: pointer;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}
</style>
