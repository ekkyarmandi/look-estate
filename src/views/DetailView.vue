<template>
  <section :id="id">
    <div class="wrapper">
      <div class="content">
        <p>ID: {{ id }}</p>
        <div class="listing-title">
          <h1>{{ title }}</h1>
          <p>{{ price_usd }}</p>
        </div>
        <div class="listing-id">
          <div class="listing-location">
            <LocationIcon />
            <p>{{ location }}</p>
          </div>
          <div class="btn-group">
            <Button class="box"><HearthIcon hideNumber="true" /></Button>
            <Button class="box btn-primary"><ShareIcon /></Button>
          </div>
        </div>
        <div class="image-container">
          <img src="@/assets/thumbnail.png" :alt="'Thumbnail of ' + title" />
          <div class="image-options">
            <img v-for:="img in images" src="@/assets/thumbnail.png" :alt="'Thumbnail of ' + title" />
          </div>
        </div>
        <PropertyDetail :data="{ contract_type, bedrooms, bathrooms, land_size, building_size }" />
        <PropertyDescription :description="description" />
      </div>
      <div class="contact">
        <GetInTouchForm />
        <ContactAgentForm />
      </div>
    </div>
  </section>
</template>

<script>
import GetInTouchForm from "@/components/forms/GetInTouchForm.vue";
import ContactAgentForm from "@/components/forms/ContactAgentForm.vue";
import PropertyDetail from "@/components/PropertyDetail.vue";
import PropertyDescription from "@/components/PropertyDescription.vue";
import HearthIcon from "@/assets/icons/HearthIcon.vue";
import LocationIcon from "@/assets/icons/LocationIcon.vue";
import ShareIcon from "@/assets/icons/ShareIcon.vue";
export default {
  name: "DetailView",
  components: {
    GetInTouchForm,
    ContactAgentForm,
    PropertyDetail,
    PropertyDescription,
    HearthIcon,
    LocationIcon,
    ShareIcon,
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
      description:
        "Peaceful Retreat with Minutes from Ubud's Top Attractions and Jungle Views\nPrice at USD 259,000 until 2053\nCompletion Date April 2025\nDiscover a sanctuary of tranquility and luxury in the heart of Bali's cultural epicenter, Ubud. This stunning off-plan villa offers a unique opportunity to immerse yourself in the serene beauty of Bali while enjoying all the modern comforts of a meticulously designed home. Priced at USD 259,000, this two-bedroom, two-bathroom villa is set on a 257 sqm plot, with a generous 182 sqm of living space, making it an ideal retreat for those seeking both relaxation and investment potential. Scheduled for completion in 2025, this villa is being offered as a leasehold property, providing an excellent long-term investment opportunity in one of Bali's most sought-after locations. The villa will come fully furnished, allowing you to move in and start enjoying your new home immediately upon completion. The furnishings have been carefully selected to complement the villa's modern tropical design, creating an atmosphere of comfort and elegance throughout.\nThe enclosed living area provides a seamless blend of indoor and outdoor living, allowing you to enjoy Bali's tropical climate while maintaining a cool, comfortable interior. The living spaces are designed to maximize the stunning jungle views, with large windows and doors that flood the villa with natural light and offer uninterrupted views of the lush greenery that surrounds the property. The two spacious bedrooms are designed as peaceful retreats, each with its own en-suite bathroom featuring modern fixtures and finishes. Wake up each morning to the sound of birdsong and the gentle rustling of leaves, and end each day with a relaxing soak in your private oasis.\nOne of the villa's most compelling features is its prime location. Just a three-minute drive from the Ubud Yoga Centre, you are perfectly positioned to take advantage of the area's vibrant wellness scene. Ubud Centre, with its bustling markets, world-class dining, and rich cultural offerings, is only ten minutes away. For those who love nature and outdoor activities, the famous Campuhan Ridge Walk is just a twelve-minute drive from your doorstep, offering breathtaking views of Ubud's iconic landscapes. Whether you're looking to make Bali your permanent home or seeking a high-yield investment property, this villa in Ubud offers the perfect combination of luxury, location, and lifestyle. With its unbeatable location, stunning jungle views, and thoughtfully designed living spaces, this villa is more than just a home it's your gateway to the best that Bali has to offer. Secure your piece of paradise today and embrace the tranquil lifestyle of Ubud.",
      images: [1, 2, 3, 4, 5],
    };
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
    attributes() {
      return {
        contract_type: this.contract_type,
        bedrooms: this.bedrooms,
        bathrooms: this.bathrooms,
        building_size: this.building_size,
        land_size: this.land_size,
      };
    },
  },
};
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
