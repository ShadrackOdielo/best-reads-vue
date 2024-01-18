<template>
  <div id="app">
    <ShelfFilter @filter-shelf="filterShelf" />
    <div class="book-container">
      <BookCard
        v-for="book in filteredBooks"
        :key="book.id"
        :book="book"
        @open-details-modal="openDetailsModal"
      />
    </div>
    <BookDetailsModal
      v-if="showDetailsModal"
      :book="selectedBook"
      @close-details-modal="closeDetailsModal"
    />
  </div>
</template>

<script>
import ShelfFilter from './components/ShelfFilter.vue';
import BookCard from './components/BookCard.vue';
import BookDetailsModal from './components/BookDetailsModal.vue';

export default {
  components: {
    ShelfFilter,
    BookCard,
    BookDetailsModal,
  },
  data() {
    return {
      books: [
        { id: 1, title: 'Book 1', author: 'Author 1', description: 'Description 1', image: 'https://via.placeholder.com/150' },
        { id: 2, title: 'Book 2', author: 'Author 2', description: 'Description 2', image: 'https://via.placeholder.com/150' },
        { id: 3, title: 'Book 3', author: 'Author 3', description: 'Description 3', image: 'https://via.placeholder.com/150' },
        // Add more books as needed
      ],
      selectedShelf: 'all',
      showDetailsModal: false,
      selectedBook: null,
    };
  },
  computed: {
    filteredBooks() {
      if (this.selectedShelf === 'all') {
        return this.books;
      }
      return this.books.filter((book) => book.shelf === this.selectedShelf);
    },
  },
  methods: {
    openDetailsModal(book) {
      this.selectedBook = book;
      this.showDetailsModal = true;
    },
    closeDetailsModal() {
      this.showDetailsModal = false;
    },
    filterShelf(shelf) {
      this.selectedShelf = shelf;
    },
  },
};
</script>

<style>
/* Add your styling here */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.book-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
</style>
