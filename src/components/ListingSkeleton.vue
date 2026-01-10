<template>
  <div class="skeleton-body">
    <div class="skeleton skeleton-thumbnail"></div>
    <div class="skeleton skeleton-text"></div>
    <div class="skeleton skeleton-text second"></div>
  </div>
</template>

<script setup>
defineOptions({
  name: "AppListingSkeleton",
});
</script>

<style scoped>
.skeleton-body {
  min-width: 375px;
  display: flex;
  gap: 12px;
  flex-direction: column;
  margin-bottom: 20px;
}

.skeleton-thumbnail {
  width: 100%;
  aspect-ratio: 4/3;
  background-color: #cbd5e1;
  border-radius: 12px;
  position: relative;
  overflow: hidden;
}
.skeleton-text {
  height: 20px;
  background-color: #cbd5e1;
  position: relative;
  overflow: hidden;
}

.second {
  width: 70%;
}

.skeleton::after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  transform: translateX(-100%);
  background-image: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0) 0,
    rgba(255, 255, 255, 0.2) 20%,
    rgba(255, 255, 255, 0.5) 60%,
    rgba(255, 255, 255, 0)
  );
  animation: shimmer 2s infinite;
}

@keyframes shimmer {
  100% {
    transform: translateX(100%);
  }
}
</style>
