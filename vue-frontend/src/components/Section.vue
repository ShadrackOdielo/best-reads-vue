<template>
  <div class="section">
    <h2>{{ title }}</h2>
    <div class="book-container">
      <BookCard
        v-for="book in books"
        :key="book.id"
        :book="book"
        :isAuthenticated="isAuthenticated"
        :shelves="shelves"
      />
    </div>
  </div>
</template>

<script>
import BookCard from './BookCard.vue';

export default {
  components: {
    BookCard,
  },
  props: {
    title: String,
    books: Array,
    isAuthenticated: Boolean,
    shelves: Array,
  },
};
</script>

<style scoped>
/* Add your styling here */
.section {
  margin-bottom: 20px;
}

.book-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
</style>
