<template>
  <div class="listing-attribute">
    <div class="attribute-item">
      <div class="item">
        <ScriptIcon />
        <p class="value">{{ data.contract_type }}</p>
      </div>
      <p class="attribute-title">Contract Type</p>
    </div>
    <div class="attribute-item">
      <div class="item">
        <BedIcon />
        <p class="value">{{ data.bedrooms }}</p>
      </div>
      <p class="attribute-title">Bedrooms</p>
    </div>
    <div class="attribute-item">
      <div class="item">
        <BathIcon />
        <p class="value">{{ data.bathrooms }}</p>
      </div>
      <p class="attribute-title">Bathrooms</p>
    </div>
    <div class="attribute-item">
      <div class="item">
        <AreaIcon />
        <p class="value">{{ landSize }} <span>sqm</span></p>
      </div>
      <p class="attribute-title">Land Size</p>
    </div>
    <div class="attribute-item">
      <div class="item">
        <BuildingIcon />
        <p class="value">{{ buildingSize }} <span>sqm</span></p>
      </div>
      <p class="attribute-title">Building Size</p>
    </div>
  </div>
</template>

<script>
import ScriptIcon from "@/assets/icons/ScriptIcon.vue";
import BedIcon from "@/assets/icons/BedIcon.vue";
import BathIcon from "@/assets/icons/BathIcon.vue";
import AreaIcon from "@/assets/icons/AreaIcon.vue";
import BuildingIcon from "@/assets/icons/BuildingIcon.vue";
export default {
  name: "PropertyDetail",
  props: ["data"],
  components: {
    ScriptIcon,
    BedIcon,
    BathIcon,
    AreaIcon,
    BuildingIcon,
  },
  computed: {
    buildingSize() {
      return this.data.building_size.toLocaleString("en-Us");
    },
    landSize() {
      return this.data.land_size.toLocaleString("en-Us");
    },
  },
};
</script>

<style scoped>
.listing-attribute {
  display: flex;
  justify-content: center;
  gap: 8px;
  background-color: white;
  border-radius: 12px;
  padding: 28px;
}
.item {
  display: flex;
  gap: 8px;
  margin-bottom: 8px;
}
.item .value {
  font-size: 16px;
}
.item span {
  font-size: 12px;
}
.attribute-item {
  padding: 4px 8px;
}
.attribute-title {
  font-size: 14px;
  color: #999;
}
</style>
