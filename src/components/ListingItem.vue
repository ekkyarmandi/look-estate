<template>
  <div class="listing-item">
    <img src="@/assets/thumbnail.png" :alt="'Thumbnail of ' + title" />
    <div class="title-wrapper">
      <h2>{{ title }}</h2>
      <p class="price">{{ price_usd }}</p>
    </div>
    <div class="badges">
      <Badge
        ><HashIcon />
        <p>{{ id }}</p></Badge
      >
      <Badge
        ><BedIcon />
        <p>{{ bedrooms }}</p></Badge
      >
      <Badge
        ><BathIcon />
        <p>{{ bathrooms }}</p></Badge
      >
      <Badge
        ><BuildingIcon />
        <p>{{ buildingSize }} sqm</p></Badge
      >
      <Badge
        ><AreaIcon />
        <p>{{ landSize }} sqm</p></Badge
      >
      <Badge
        ><ScriptIcon />
        <p>{{ contract_type }}</p></Badge
      >
    </div>
  </div>
</template>

<script>
import Badge from "@/components/Badge.vue";
import HashIcon from "@/assets/icons/HashIcon.vue";
import BedIcon from "@/assets/icons/BedIcon.vue";
import BathIcon from "@/assets/icons/BathIcon.vue";
import BuildingIcon from "@/assets/icons/BuildingIcon.vue";
import AreaIcon from "@/assets/icons/AreaIcon.vue";
import ScriptIcon from "@/assets/icons/ScriptIcon.vue";
export default {
  name: "ListingItem",
  components: {
    Badge,
    HashIcon,
    BedIcon,
    BathIcon,
    BuildingIcon,
    AreaIcon,
    ScriptIcon,
  },
  computed: {
    price_usd() {
      return this.price
        .toLocaleString("en-US", {
          style: "currency",
          currency: "USD",
        })
        .replace(".00", "");
    },
    buildingSize() {
      return this.building_size.toLocaleString("en-Us");
    },
    landSize() {
      return this.land_size.toLocaleString("en-Us");
    },
  },
  data() {
    return {
      id: "436393",
      title: "Charming One Bedroom Villa in Ubud with A Spacious Garden",
      location: "Ubud, Bali",
      contract_type: "Leasehold",
      price: 10000,
      bedrooms: 2,
      bathrooms: 2,
      building_size: 1234,
      land_size: 1234,
    };
  },
};
</script>

<style scoped>
.listing-item {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.listing-item img {
  height: 320px;
  border-radius: 8px;
}
h2 {
  font-size: 20px;
}
.title-wrapper {
  display: flex;
  justify-content: space-between;
  color: var(--secondary-500);
}
.price {
  font-size: 18px;
  font-weight: 600;
}
.badges {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}
.badges p {
  font-size: 1rem;
}
</style>
