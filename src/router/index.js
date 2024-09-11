import { createRouter, createWebHistory } from "vue-router";
import ListingContainer from "@/components/ListingContainer.vue";
import PropertyDetailView from "../views/PropertyDetailView.vue";
import BookmarkView from "../views/BookmarkView.vue";

const routes = [
  {
    path: "/",
    name: "ListingContainer",
    component: ListingContainer,
  },
  {
    path: "/properties/:id",
    name: "PropertyDetail",
    component: PropertyDetailView,
    props: true,
  },
  {
    path: "/bookmarks",
    name: "Bookmarks",
    component: BookmarkView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
