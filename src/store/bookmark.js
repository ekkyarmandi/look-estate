import { defineStore } from "pinia";

export const useBookmarkStore = defineStore("bookmarkStore", {
  state: () => ({
    bookmarked: [],
  }),
  actions: {
    addBookmark(bookmark) {
      this.bookmarked.push(bookmark);
    },
    removeBookmark(bookmark) {
      this.bookmarked = this.bookmarked.filter((b) => b !== bookmark);
    },
  },
  getters: {
    total: (state) => state.bookmarked.length,
  },
  persist: true,
});
