<template>
  <ResultFound/>
  <ListingContainer/>
</template>

<script>
import ResultFound from "@/components/ResultFound.vue";
import ListingContainer from "@/components/ListingContainer.vue";

export default {
  name: 'HomeView',
  components: {
    ResultFound,
    ListingContainer
  }
}
</script>
