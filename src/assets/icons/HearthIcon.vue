<template>
  <div v-if="!hideNumber" class="whistlist">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M19 14C20.49 12.54 22 10.79 22 8.5C22 7.04131 21.4205 5.64236 20.3891 4.61091C19.3576 3.57946 17.9587 3 16.5 3C14.74 3 13.5 3.5 12 5C10.5 3.5 9.26 3 7.5 3C6.04131 3 4.64236 3.57946 3.61091 4.61091C2.57946 5.64236 2 7.04131 2 8.5C2 10.8 3.5 12.55 5 14L12 21L19 14Z"
        :stroke="color"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
    <div><p>9</p></div>
  </div>
  <div v-if="hideNumber" :class="['heart-icon', { 'custom-color': !color }]">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M19 14C20.49 12.54 22 10.79 22 8.5C22 7.04131 21.4205 5.64236 20.3891 4.61091C19.3576 3.57946 17.9587 3 16.5 3C14.74 3 13.5 3.5 12 5C10.5 3.5 9.26 3 7.5 3C6.04131 3 4.64236 3.57946 3.61091 4.61091C2.57946 5.64236 2 7.04131 2 8.5C2 10.8 3.5 12.55 5 14L12 21L19 14Z"
        :stroke="color"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
  </div>
</template>

<script>
export default {
  name: "HearthIcon",
  props: {
    hideNumber: {
      type: Boolean,
      default: false,
    },
    color: {
      type: String,
      default: "#30485E",
    },
  },
};
</script>

<style scoped>
.custom-color {
  --path-stroke: var(--secondary-500);
}
.cutom-color:hover {
  --path-stroke: var(--secondary-400);
}
.custom-color svg path {
  stroke: var(--path-stroke);
}
.whistlist {
  position: relative;
  margin-right: 0.5rem;
  cursor: pointer;
  width: 36px;
  height: 30px;
}
.whistlist svg {
  position: absolute;
  left: 0;
  bottom: 0;
}
.whistlist div {
  position: absolute;
  top: 0;
  right: 0;
}
.whistlist p {
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--primary-500);
  color: white;
  width: 18px;
  height: 18px;
  font-size: 12px;
  border: 1px solid white;
  border-radius: 50%;
}
.heart-icon {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
